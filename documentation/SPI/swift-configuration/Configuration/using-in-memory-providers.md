---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/using-in-memory-providers"
framework: "swift-configuration/Configuration"
---

# Using in-memory providers

**Framework**: swift-configuration/Configuration  
**Role**: Article

Learn about the [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) built-in types.

#### Overview

Swift Configuration provides two in-memory providers, which you directly instantiate with the desired keys and values, rather than parsing them from another representation. These providers are particularly useful for testing, providing fallback values, and bridging with other configuration systems.

- [`InMemoryProvider`](./inmemoryprovider.md) is an immutable value type, and can be useful for defining overrides and fallbacks in a provider hierarchy.
- [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) is a mutable reference type, allowing you to update values and automatically notifying any watchers. It can be used to bridge from other stateful, callback-based configuration sources.

##### InMemoryProvider

The [`InMemoryProvider`](./inmemoryprovider.md) is ideal for static configuration values that don’t change during application runtime.

###### Basic usage

Create an [`InMemoryProvider`](./inmemoryprovider.md) with a dictionary of configuration values:

```swift
let provider = InMemoryProvider(values: [
    "database.host": "localhost",
    "database.port": 5432,
    "api.timeout": 30.0,
    "debug.enabled": true
])

let config = ConfigReader(provider: provider)
let host = config.string(forKey: "database.host") // "localhost"
let port = config.int(forKey: "database.port") // 5432
```

###### Using with hierarchical keys

You can use [`AbsoluteConfigKey`](./absoluteconfigkey.md) for more complex key structures:

```swift
let provider = InMemoryProvider(values: [
    AbsoluteConfigKey(["http", "client", "timeout"]): 30.0,
    AbsoluteConfigKey(["http", "server", "port"]): 8080,
    AbsoluteConfigKey(["logging", "level"]): "info"
])
```

###### Configuration context

The in-memory provider performs exact matching of config keys, including the context. This allows you to provide different values for the same key path based on contextual information.

The following example shows using two keys with the same key path, but different context, and giving them two different values:

```swift
let provider = InMemoryProvider(
    values: [
        AbsoluteConfigKey(
            ["http", "client", "timeout"], 
            context: ["upstream": "example1.org"]
        ): 15.0,
        AbsoluteConfigKey(
            ["http", "client", "timeout"], 
            context: ["upstream": "example2.org"]
        ): 30.0,
    ]
)
```

When you configure a provider this way, a config reader will return the following results:

```swift
let config = ConfigReader(provider: provider)
config.double(forKey: "http.client.timeout") // nil
config.double(
    forKey: ConfigKey(
        "http.client.timeout", 
        context: ["upstream": "example1.org"]
    )
) // 15.0
config.double(
    forKey: ConfigKey(
        "http.client.timeout",
        context: ["upstream": "example2.org"]
    )
) // 30.0
```

##### MutableInMemoryProvider

The [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) allows you to modify configuration values at runtime and notify watchers of changes.

###### Basic usage

```swift
let provider = MutableInMemoryProvider()
provider.setValue("localhost", forKey: "database.host")
provider.setValue(5432, forKey: "database.port")

let config = ConfigReader(provider: provider)
let host = config.string(forKey: "database.host") // "localhost"
```

###### Updating values

You can update values after creation, and the provider notifies any watchers:

```swift
// Initial setup
provider.setValue("debug", forKey: "logging.level")

// Later in your application, watchers are notified
provider.setValue("info", forKey: "logging.level") 
```

###### Watching for changes

Use the provider’s async sequence to watch for configuration changes:

```swift
let config = ConfigReader(provider: provider)
try await config.watchString(
    forKey: "logging.level",
    as: Logger.Level.self,
    default: .debug
) { updates in
    for try await level in updates {
        print("Logging level changed to: \(level)")
    }
}
```

##### Common Use Cases

###### Testing

In-memory providers are excellent for unit testing:

```swift
func testDatabaseConnection() {
    let testProvider = InMemoryProvider(values: [
        "database.host": "test-db.example.com",
        "database.port": 5433,
        "database.name": "test_db"
    ])
    
    let config = ConfigReader(provider: testProvider)
    let connection = DatabaseConnection(config: config)
    // Test your database connection logic
}
```

###### Fallback values

Use [`InMemoryProvider`](./inmemoryprovider.md) as a fallback in a provider hierarchy:

```swift
let fallbackProvider = InMemoryProvider(values: [
    "api.timeout": 30.0,
    "retry.maxAttempts": 3,
    "cache.enabled": true
])

let config = ConfigReader(providers: [
    EnvironmentVariablesProvider(),
    fallbackProvider 
    // Used when environment variables are not set
])
```

###### Bridging other systems

Use [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) to bridge configuration from other systems:

```swift
class ConfigurationBridge {
    private let provider = MutableInMemoryProvider()
    
    func updateFromExternalSystem(_ values: [String: ConfigValue]) {
        for (key, value) in values {
            provider.setValue(value, forKey: key)
        }
    }
}
```

For comparison with reloading providers, see [Using reloading providers](./using-reloading-providers.md). To understand different access patterns and when to use each provider type, check out [Choosing the access pattern](./choosing-access-patterns.md). For more configuration guidance, refer to [Adopting best practices](./best-practices.md).

## See Also

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
- [struct InMemoryProvider](./inmemoryprovider.md)
  A configuration provider that stores values in memory.
- [class MutableInMemoryProvider](./mutableinmemoryprovider.md)
  A configuration provider that stores mutable values in memory.
- [struct KeyMappingProvider](./keymappingprovider.md)
  A configuration provider that maps all keys before delegating to an upstream provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/using-in-memory-providers)*