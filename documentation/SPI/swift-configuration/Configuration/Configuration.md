---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration"
framework: "swift-configuration/Configuration"
---

# Configuration

**Framework**: swift-configuration/Configuration  
**Kind**: module  
**Role**: Library

A Swift library for reading configuration in applications and libraries.

#### Overview

Swift Configuration defines an abstraction between configuration *readers* and *providers*.

Applications and libraries *read* configuration through a consistent API, while you set up the actual *provider* once at your application’s entry point.

For example, to read the timeout configuration value for an HTTP client, check out the following examples using different providers:

**Environment variables**:

```env
# Environment variables:
HTTP_TIMEOUT=30
```

```swift
let provider = EnvironmentVariablesProvider()
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**Command line arguments**:

```bash
# Program invoked with:
program --http-timeout 30
```

```swift
let provider = CommandLineArgumentsProvider()
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**JSON**:

```json
{
  "http": {
    "timeout": 30
  }
}
```

```swift
let provider = try await FileProvider<JSONSnapshot>(
    filePath: "/etc/config.json"
)
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**Reloading JSON**:

```json
{
  "http": {
    "timeout": 30
  }
}
```

```swift
let provider = try await ReloadingFileProvider<JSONSnapshot>(
    filePath: "/etc/config.json"
)
// Omitted: Add `provider` to a ServiceGroup
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**YAML**:

```yaml
http:
  timeout: 30
```

```swift
let provider = try await FileProvider<YAMLSnapshot>(
    filePath: "/etc/config.yaml"
)
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**Reloading YAML**:

```yaml
http:
  timeout: 30
```

```swift
let provider = try await ReloadingFileProvider<YAMLSnapshot>(
    filePath: "/etc/config.yaml"
)
// Omitted: Add `provider` to a ServiceGroup
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**Property list**:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>http</key>
    <dict>
        <key>timeout</key>
        <integer>30</integer>
    </dict>
</dict>
</plist>
```

```swift
let provider = try await FileProvider<PropertyListSnapshot>(
    filePath: "/etc/config.plist"
)
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**Directory files**:

```swift
/
|-- run
    |-- secrets
        |-- http-timeout
```

Contents of the file `/run/secrets/http-timeout`: `30`.

```swift
let provider = try await DirectoryFilesProvider(
    directoryPath: "/run/secrets"
)
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**Provider hierarchy**:

```swift
// Environment variables consulted first, then JSON.
let primaryProvider = EnvironmentVariablesProvider()
let secondaryProvider = try await FileProvider<JSONSnapshot>(
    filePath: "/etc/config.json"
)
let config = ConfigReader(providers: [
    primaryProvider,
    secondaryProvider
])
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

**In-memory**:

```swift
let provider = InMemoryProvider(values: [
    "http.timeout": 30,
])
let config = ConfigReader(provider: provider)
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print(httpTimeout) // prints 30
```

For a selection of more detailed examples, read through [Example use cases](./example-use-cases.md).

For a video introduction, check out our [talk on YouTube](https://www.youtube.com/watch?v=I3lYW6OEyIs).

If you’re migrating from manually handling configuration, the [Migrating to Swift Configuration](./migrating-to-swift-configuration.md) guide walks through the transition step by step.

You can combine these providers to form a hierarchy. For details, check out [Provider hierarchy](./Configuration.md#Provider-hierarchy).

##### Quick start

Add the dependency to your `Package.swift`:

```swift
.package(url: "https://github.com/apple/swift-configuration", from: "1.0.0")
```

Add the library dependency to your target:

```swift
.product(name: "Configuration", package: "swift-configuration")
```

Import and use in your code:

```swift
import Configuration

let config = ConfigReader(provider: EnvironmentVariablesProvider())
let httpTimeout = config.int(forKey: "http.timeout", default: 60)
print("The HTTP timeout is: \(httpTimeout)")
```

##### Package traits

This package offers additional integrations you can enable using [package traits](https://docs.swift.org/swiftpm/documentation/packagemanagerdocs/addingdependencies#Packages-with-Traits). To enable an additional trait on the package, update the package dependency:

```diff
.package(
    url: "https://github.com/apple/swift-configuration",
    from: "1.0.0",
+   traits: [.defaults, "YAML"]
)
```

Available traits:

- **`JSON`** (default): Adds support for [`JSONSnapshot`](./jsonsnapshot.md), which enables using [`FileProvider`](./fileprovider.md) and [`ReloadingFileProvider`](./reloadingfileprovider.md) with JSON files.
- **`Logging`** (opt-in): Adds support for [`AccessLogger`](./accesslogger.md), a way to emit access events into a Swift Log `Logger`.
- **`Reloading`** (opt-in): Adds support for [`ReloadingFileProvider`](./reloadingfileprovider.md), which provides auto-reloading capability for file-based configuration.
- **`CommandLineArguments`** (opt-in): Adds support for [`CommandLineArgumentsProvider`](./commandlineargumentsprovider.md) for parsing command line arguments.
- **`YAML`** (opt-in): Adds support for [`YAMLSnapshot`](./yamlsnapshot.md), which enables using [`FileProvider`](./fileprovider.md) and [`ReloadingFileProvider`](./reloadingfileprovider.md) with YAML files.
- **`PropertyList`** (opt-in): Adds support for [`PropertyListSnapshot`](./propertylistsnapshot.md), which enables using [`FileProvider`](./fileprovider.md) and [`ReloadingFileProvider`](./reloadingfileprovider.md) with property list files.

##### Supported platforms and minimum versions

The library is supported on Apple platforms, Linux, Windows, and Android.

- macOS 15+
- iOS 18+
- tvOS 18+
- watchOS 11+
- visionOS 2+
- Linux
- Windows
- Android API 28+

##### Key features

###### Three access patterns

The library provides three distinct ways to read configuration values:

- **Get**: Synchronously return the current value available locally, in memory:

  ```swift
  let timeout = config.int(forKey: "http.timeout", default: 60)
  ```
- **Fetch**: Asynchronously get the most up-to-date value from disk or a remote server:

  ```swift
  let timeout = try await config.fetchInt(forKey: "http.timeout", default: 60)
  ```
- **Watch**: Receive updates when a configuration value changes:

  ```swift
  try await config.watchInt(forKey: "http.timeout", default: 60) { updates in
      for try await timeout in updates {
          print("HTTP timeout updated to: \(timeout)")
      }
  }
  ```

For detailed guidance on when to use each access pattern, see [Choosing the access pattern](./choosing-access-patterns.md). Within each of the access patterns, the library offers different reader methods that reflect your needs of optional, default, and required configuration parameters. To understand the choices available, see [Choosing reader methods](./choosing-reader-methods.md).

###### Providers

###### Built-in providers

The library includes comprehensive built-in provider support:

- Environment variables: [`EnvironmentVariablesProvider`](./environmentvariablesprovider.md)
- Command-line arguments: [`CommandLineArgumentsProvider`](./commandlineargumentsprovider.md)
- JSON file: [`FileProvider`](./fileprovider.md) and [`ReloadingFileProvider`](./reloadingfileprovider.md) with [`JSONSnapshot`](./jsonsnapshot.md)
- YAML file: [`FileProvider`](./fileprovider.md) and [`ReloadingFileProvider`](./reloadingfileprovider.md) with [`YAMLSnapshot`](./yamlsnapshot.md)
- Property list file: [`FileProvider`](./fileprovider.md) and [`ReloadingFileProvider`](./reloadingfileprovider.md) with [`PropertyListSnapshot`](./propertylistsnapshot.md)
- Directory of files: [`DirectoryFilesProvider`](./directoryfilesprovider.md)
- In-memory: [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md)
- Key transforming: [`KeyMappingProvider`](./keymappingprovider.md)

###### Community providers

- TOML file: [mattt/swift-configuration-toml](https://github.com/mattt/swift-configuration-toml)

You can also implement a custom [`ConfigProvider`](./configprovider.md).

###### Provider hierarchy

In addition to using providers individually, you can create fallback behavior using an array of providers. The first provider that returns a non-nil value wins.

The following example shows a provider hierarchy where environment variables take precedence over command line arguments, a JSON file, and in-memory defaults:

```swift
// Create a hierarchy of providers with fallback behavior.
let config = ConfigReader(providers: [
    // First, check environment variables.
    EnvironmentVariablesProvider(),
    // Then, check command-line options.
    CommandLineArgumentsProvider(),
    // Then, check a JSON config file.
    try await FileProvider<JSONSnapshot>(filePath: "/etc/config.json"),
    // Finally, fall back to in-memory defaults.
    InMemoryProvider(values: [
        "http.timeout": 60,
    ])
])

// Uses the first provider that has a value for "http.timeout".
let timeout = config.int(forKey: "http.timeout", default: 15)
```

###### Hot reloading

You can periodically reload configuration in long-running services with [`ReloadingFileProvider`](./reloadingfileprovider.md):

```swift
let provider = try await ReloadingFileProvider<JSONSnapshot>(filePath: "/etc/config.json")
// Omitted: add provider to a ServiceGroup
let config = ConfigReader(provider: provider)

try await config.watchInt(forKey: "http.timeout", default: 60) { updates in
    for try await timeout in updates {
        print("HTTP timeout updated to: \(timeout)")
    }
}
```

Read [Using reloading providers](./using-reloading-providers.md) for details on how to receive updates as configuration changes.

###### Namespacing and scoped readers

The built-in namespacing of [`ConfigKey`](./configkey.md) interprets `"http.timeout"` as an array of two components: `"http"` and `"timeout"`. The following example uses [`scoped(to:)`](./configreader/scoped%28to%29.md) to create a namespaced reader with the key `"http"`, to allow reads to use the shorter key `"timeout"`:

Consider the following JSON configuration:

```json
{
  "http": {
    "timeout": 60
  }
}
```

```swift
// Create the root reader.
let config = ConfigReader(provider: provider)

// Create a scoped reader for HTTP settings.
let httpConfig = config.scoped(to: "http")

// Now you can access values with shorter keys.
// Equivalent to reading "http.timeout" on the root reader.
let timeout = httpConfig.int(forKey: "timeout")
```

###### Debugging and troubleshooting

Use [`AccessReporter`](./accessreporter.md) to log all accesses to a config reader:

```swift
let logger = Logger(label: "config")
let config = ConfigReader(
    provider: provider,
    accessReporter: AccessLogger(logger: logger)
)
// Now all configuration access is logged, with secret values redacted
```

You can also add the following environment variable to emit access logs to a file without any code changes:

```env
CONFIG_ACCESS_LOG_FILE=/var/log/myapp/config-access.log
```

and then read the file:

```zsh
tail -f /var/log/myapp/config-access.log
```

Check out the built-in [`AccessLogger`](./accesslogger.md), [`FileAccessLogger`](./fileaccesslogger.md), and [Troubleshooting and access reporting](./troubleshooting.md).

###### Handling Secrets

The library provides built-in support for handling sensitive configuration values securely:

```swift
// Mark sensitive values as secrets to prevent them from appearing in logs
let privateKey = try snapshot.requiredString(forKey: "mtls.privateKey", isSecret: true)
let optionalAPIToken = config.string(forKey: "api.token", isSecret: true)
```

When you mark values as secrets, the library automatically redacts them from access logs and debugging output. Read [Handling secrets correctly](./handling-secrets-correctly.md) for guidance on best practices for secrets management.

###### Consistent snapshots

Retrieve related values from a consistent snapshot using [`ConfigSnapshotReader`](./configsnapshotreader.md), which [`snapshot()`](./configreader/snapshot%28%29.md) returns.

This ensures that you read multiple values from a single snapshot inside each provider, even when using providers that update their internal values. For example by downloading new data periodically:

```swift
let config = /* a reader with one or more providers that change values over time */
let snapshot = config.snapshot()
let certificate = try snapshot.requiredString(forKey: "mtls.certificate")
let privateKey = try snapshot.requiredString(forKey: "mtls.privateKey", isSecret: true)
// `certificate` and `privateKey` are guaranteed to come from the same snapshot in the provider
```

###### Extensible ecosystem

Any package can implement a [`ConfigProvider`](./configprovider.md), making the ecosystem extensible for custom configuration sources.

## Topics

### Essentials
- [Configuring applications](./configuring-applications.md)
  Provide flexible and consistent configuration for your application.
- [Configuring libraries](./configuring-libraries.md)
  Provide a consistent and flexible way to configure your library.
- [Example use cases](./example-use-cases.md)
  Review common use cases with ready-to-copy code samples.
- [Migrating to Swift Configuration](./migrating-to-swift-configuration.md)
  Evolve from manual configuration reading to unified, production-ready configuration.
- [Adopting best practices](./best-practices.md)
  Follow these principles to make your code easily configurable and composable with other libraries.
### Readers and providers
- [struct ConfigReader](./configreader.md)
  A type that provides read-only access to configuration values from underlying providers.
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
### Built-in providers
- [struct EnvironmentVariablesProvider](./environmentvariablesprovider.md)
  A configuration provider that reads values from environment variables.
- [struct CommandLineArgumentsProvider](./commandlineargumentsprovider.md)
  A configuration provider that sources values from command-line arguments.
- [Integrating with Swift Argument Parser](./integrating-with-swift-argument-parser.md)
  Combine the commands and options of Swift Argument Parser with the provider hierarchy of Swift Configuration.
- [struct FileProvider](./fileprovider.md)
  A configuration provider that reads from a file on disk using a configurable snapshot type.
- [class ReloadingFileProvider](./reloadingfileprovider.md)
  A configuration provider that reads configuration from a file on disk with automatic reloading capability.
- [struct JSONSnapshot](./jsonsnapshot.md)
  A snapshot of configuration values parsed from JSON data.
- [class YAMLSnapshot](./yamlsnapshot.md)
  A snapshot of configuration values parsed from YAML data.
- [struct PropertyListSnapshot](./propertylistsnapshot.md)
  A snapshot of configuration values parsed from property list (plist) data.
- [Using reloading providers](./using-reloading-providers.md)
  Automatically reload configuration from files when they change.
- [struct DirectoryFilesProvider](./directoryfilesprovider.md)
  A configuration provider that reads values from individual files in a directory.
- [Using in-memory providers](./using-in-memory-providers.md)
  Learn about the [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) built-in types.
- [struct InMemoryProvider](./inmemoryprovider.md)
  A configuration provider that stores values in memory.
- [class MutableInMemoryProvider](./mutableinmemoryprovider.md)
  A configuration provider that stores mutable values in memory.
- [struct KeyMappingProvider](./keymappingprovider.md)
  A configuration provider that maps all keys before delegating to an upstream provider.
### Creating a custom provider
- [Implementing a custom provider](./implementing-a-provider.md)
  Create a custom configuration provider to integrate a new data source.
- [protocol ConfigSnapshot](./configsnapshot.md)
  An immutable snapshot of a configuration provider’s state.
- [protocol FileConfigSnapshot](./fileconfigsnapshot.md)
  A protocol for configuration snapshots created from file data.
- [protocol FileParsingOptions](./fileparsingoptions.md)
  A type that provides parsing options for file configuration snapshots.
- [protocol ConfigProvider](./configprovider.md)
  A type that provides configuration values from a data source.
- [enum ConfigContent](./configcontent.md)
  The raw content of a configuration value.
- [struct ConfigValue](./configvalue.md)
  A configuration value that wraps content with metadata.
- [enum ConfigType](./configtype.md)
  The supported configuration value types.
- [struct LookupResult](./lookupresult.md)
  The result of looking up a configuration value in a provider.
- [enum SecretsSpecifier](./secretsspecifier.md)
  A specification for identifying which configuration values contain sensitive information.
- [struct ConfigUpdatesAsyncSequence](./configupdatesasyncsequence.md)
  A concrete async sequence for delivering updated configuration values.
### Configuration keys
- [struct ConfigKey](./configkey.md)
  A configuration key representing a relative path to a configuration value.
- [struct AbsoluteConfigKey](./absoluteconfigkey.md)
  A configuration key that represents an absolute path to a configuration value.
- [enum ConfigContextValue](./configcontextvalue.md)
  A value that can be stored in a configuration context.
### Troubleshooting and access reporting
- [Troubleshooting and access reporting](./troubleshooting.md)
  Check out some techniques to debug unexpected issues and to increase visibility into accessed config values.
- [protocol AccessReporter](./accessreporter.md)
  A type that receives and processes configuration access events.
- [class AccessLogger](./accesslogger.md)
  An access reporter that logs configuration access events using the Swift Log API.
- [class FileAccessLogger](./fileaccesslogger.md)
  An access reporter that writes configuration access events to a file.
- [struct AccessEvent](./accessevent.md)
  An event that captures information about accessing a configuration value.
- [struct BroadcastingAccessReporter](./broadcastingaccessreporter.md)
  An access reporter that forwards events to multiple other reporters.
### Value conversion
- [protocol ExpressibleByConfigString](./expressiblebyconfigstring.md)
  A protocol for types that can be initialized from configuration string values.
- [protocol ExpressibleByConfigInt](./expressiblebyconfigint.md)
  A protocol for types that can be initialized from configuration integer values.
- [protocol ConfigBytesFromStringDecoder](./configbytesfromstringdecoder.md)
  A protocol for decoding string configuration values into byte arrays.
- [struct ConfigBytesFromBase64StringDecoder](./configbytesfrombase64stringdecoder.md)
  A decoder that converts base64-encoded strings into byte arrays.
- [struct ConfigBytesFromHexStringDecoder](./configbytesfromhexstringdecoder.md)
  A decoder that converts hexadecimal-encoded strings into byte arrays.
### Contributing
- [Developing Swift Configuration](./development.md)
  Learn about tools and conventions used to develop the Swift Configuration package.
- [Proposals](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/proposals)
  Collaborate on API changes to Swift Configuration by writing a proposal.
### Extended Modules
- [Foundation](./foundation.md)
- [Swift](./swift.md)
- [SystemPackage](./systempackage.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration)*