---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader"
framework: "swift-configuration/Configuration"
---

# ConfigReader

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A type that provides read-only access to configuration values from underlying providers.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfigReader
```

## Mentions

- [Migrating to Swift Configuration](./migrating-to-swift-configuration.md)
- [Configuring libraries](./configuring-libraries.md)
- [Example use cases](./example-use-cases.md)
- [Integrating with Swift Argument Parser](./integrating-with-swift-argument-parser.md)
- [Using reloading providers](./using-reloading-providers.md)

## Overview

Use `ConfigReader` to access configuration values from various sources like environment variables, JSON files, or in-memory stores. The reader supports provider hierarchies, key scoping, and access reporting for debugging configuration usage.

## Usage

To read configuration values, create a config reader with one or more providers:

```swift
let config = ConfigReader(provider: EnvironmentVariablesProvider())
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
```

### Using multiple providers

Create a hierarchy of providers by passing an array to the initializer. The reader queries providers in order, using the first non-nil value it finds:

```swift
do {
    let config = ConfigReader(providers: [
        // First, check environment variables
        EnvironmentVariablesProvider(),
        // Then, check a JSON config file
        try await FileProvider<JSONSnapshot>(filePath: "/etc/config.json"),
        // Finally, fall back to in-memory defaults
        InMemoryProvider(values: [
            "http.timeout": 60,
        ])
    ])

    // Uses the first provider that has a value for "http.timeout"
    let timeout = config.int(forKey: "http.timeout", default: 15)
} catch {
    print("Failed to create JSON provider: \(error)")
}
```

The `get` and `fetch` methods query providers sequentially, while the `watch` method monitors all providers in parallel and returns the first non-nil value from the latest results.

### Creating scoped readers

Create a scoped reader to access nested configuration sections without repeating key prefixes. This is useful for passing configuration to specific components.

Given this JSON configuration:

```json
{
  "http": {
    "timeout": 60
  }
}
```

Create a scoped reader for the HTTP section:

```swift
let httpConfig = config.scoped(to: "http")
let timeout = httpConfig.int(forKey: "timeout")  // Reads "http.timeout"
```

### Understanding config keys

The library accesses configuration values using config keys that represent a hierarchical path to the value. Internally, the library represents a key as a list of string components, such as `["http", "timeout"]`.

### Using configuration context

Provide additional context to help providers return more specific values. In the following example with a configuration that includes repeated configurations per “upstream”, the value returned is potentially constrained to the configuration with the matching context:

```swift
let httpTimeout = config.int(
    forKey: ConfigKey("http.timeout", context: ["upstream": "example.com"]),
    default: 60
)
```

Providers can use this context to return specialized values or fall back to generic ones. Some providers may ignore context and use only the key path.

### Automatic type conversion

The library can automatically convert string or int configuration values to other types using the `as:` parameter. This works with:

- String or Int backed enum types, as they conform to `RawRepresentable<String>` or `RawRepresentable<Int>`.
- Types that you explicitly conform to [`ExpressibleByConfigString`](./expressiblebyconfigstring.md) or [`ExpressibleByConfigInt`](./expressiblebyconfigint.md).
- Built-in types that already conform to [`ExpressibleByConfigString`](./expressiblebyconfigstring.md):

  - `SystemPackage.FilePath` - Converts from file paths.
  - `Foundation.URL` - Converts from URL strings.
  - `Foundation.UUID` - Converts from UUID strings.
  - `Foundation.Date` - Converts from ISO8601 date strings.
- Built-in types that already conform to [`ExpressibleByConfigInt`](./expressiblebyconfigint.md):
- `Swift.Duration` - Converts from an integer value to a Duration measured in seconds.

```swift
// Built-in type conversion
let apiUrl = config.string(forKey: "api.url", as: URL.self)
let requestId = config.string(
    forKey: "request.id",
    as: UUID.self
)

// Custom enum conversion (RawRepresentable<String>)
enum LogLevel: String {
    case debug, info, warning, error
}
let logLevel = config.string(
    forKey: "logging.level",
    as: LogLevel.self,
    default: .info
)

// Custom type conversion (ExpressibleByConfigString)
struct DatabaseURL: ExpressibleByConfigString {
    let url: URL

    init?(configString: String) {
        guard let url = URL(string: configString) else { return nil }
        self.url = url
    }

    var description: String { url.absoluteString }
}
let dbUrl = config.string(
    forKey: "database.url",
    as: DatabaseURL.self
)
```

### How providers encode keys

Each [`ConfigProvider`](./configprovider.md) interprets config keys according to its data source format. For example, [`EnvironmentVariablesProvider`](./environmentvariablesprovider.md) converts `["http", "timeout"]` to the environment variable name `HTTP_TIMEOUT` by uppercasing components and joining with underscores.

### Monitoring configuration access

Use an access reporter to track which configuration values your application reads. The reporter receives [`AccessEvent`](./accessevent.md) instances containing the requested key, calling code location, returned value, and source provider.

This helps debug configuration issues and to discover the config dependencies in your codebase.

> 💡 **Tip**: Set the `CONFIG_ACCESS_LOG_FILE` environment variable to automatically log all configuration access to a file: `CONFIG_ACCESS_LOG_FILE=/tmp/config-access.log`

### Protecting sensitive values

Mark sensitive configuration values as secrets to prevent logging by access loggers. Both config readers and providers can set the `isSecret` property. When either marks a value as sensitive, [`AccessReporter`](./accessreporter.md) instances should not log the raw value.

### Configuration context

Configuration context supplements the configuration key components with extra metadata that providers can use to refine value lookups or return more specific results. Context is particularly useful for scenarios where the same configuration key might need different values based on runtime conditions.

Create context using dictionary literal syntax with automatic type inference:

```swift
let context: [String: ConfigContextValue] = [
    "environment": "production",
    "region": "us-west-2",
    "timeout": 30,
    "retryEnabled": true
]
```

#### Provider behavior

Not all providers use context information. Providers that support context can:

- Return specialized values based on context keys.
- Fall back to generic values when context doesn’t match.
- Ignore context entirely and use only the key path.

For example, a provider might return different database connection strings based on the environment context:

```swift
let dbConfig = config.string(
    forKey: ConfigKey("database.url", context: ["environment": "staging"]),
    default: "localhost:5432"
)
```

### Error handling behavior

The config reader handles provider errors differently based on the method type:

- **Get and watch methods**: Gracefully handle errors by returning `nil` or default values, except for “required” variants which rethrow errors.
- **Fetch methods**: Always rethrow both provider and conversion errors.
- **Required methods**: Rethrow all errors without fallback behavior.

The library reports all provider errors to the access reporter through the `providerResults` array, even when handled gracefully.

## Topics

### Creating config readers
- [init(provider: some ConfigProvider, accessReporter: (any AccessReporter)?)](./configreader/init%28provider,accessreporter%29.md)
  Creates a config reader with a single provider.
- [init(providers: [any ConfigProvider], accessReporter: (any AccessReporter)?)](./configreader/init%28providers,accessreporter%29.md)
  Creates a config reader with multiple providers.
### Retrieving a scoped config reader
- [func scoped(to: ConfigKey) -> ConfigReader](./configreader/scoped%28to%29.md)
  Returns a scoped config reader with the specified key appended to the current prefix.
### Reading from a snapshot
- [func snapshot() -> ConfigSnapshotReader](./configreader/snapshot%28%29.md)
  Returns a snapshot of the current configuration state.
- [func watchSnapshot<Return>(fileID: String, line: UInt, updatesHandler: nonisolated(nonsending) (ConfigUpdatesAsyncSequence<ConfigSnapshotReader, Never>) async throws -> Return) async throws -> Return](./configreader/watchsnapshot%28fileid,line,updateshandler%29.md)
  Watches the configuration for changes.
- [Synchronously reading values](./configreader-get.md)
- [Asynchronously fetching values](./configreader-fetch.md)
- [Watching values](./configreader-watch.md)
### Default Implementations
- [CustomStringConvertible Implementations](./configreader/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Readers and providers
- [protocol ConfigProvider](./configprovider.md)
  A type that provides configuration values from a data source.
- [struct ConfigSnapshotReader](./configsnapshotreader.md)
  A container type for reading config values from snapshots.
- [Choosing the access pattern](./choosing-access-patterns.md)
  Learn how to select the right method for reading configuration values based on your needs.
- [Choosing reader methods](./choosing-reader-methods.md)
  Choose between optional, default, and required variants of configuration methods.
- [Handling secrets correctly](./handling-secrets-correctly.md)
  Protect sensitive configuration values from accidental disclosure in logs and debug output.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configreader)*