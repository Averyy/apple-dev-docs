---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/inmemoryprovider"
framework: "swift-configuration/Configuration"
---

# InMemoryProvider

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration provider that stores values in memory.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct InMemoryProvider
```

## Mentions

- [Using in-memory providers](./using-in-memory-providers.md)
- [Migrating to Swift Configuration](./migrating-to-swift-configuration.md)
- [Configuring applications](./configuring-applications.md)
- [Example use cases](./example-use-cases.md)
- [Integrating with Swift Argument Parser](./integrating-with-swift-argument-parser.md)

#### Overview

This provider maintains a static dictionary of configuration values in memory, making it ideal for providing default values, overrides, or test configurations. Values are immutable once the provider is created and never change over time.

#### Use cases

The in-memory provider is particularly useful for:

- **Default configurations**: Providing fallback values when other providers don’t have a value
- **Configuration overrides**: Taking precedence over other providers
- **Testing**: Creating predictable configuration states for unit tests
- **Static configurations**: Embedding compile-time configuration values

#### Value types

The provider supports all standard configuration value types and automatically handles type validation. Values must match the requested type exactly - no automatic conversion is performed - for example, requesting a `String` value for a key that stores an `Int` value will throw an error.

#### Performance characteristics

This provider offers O(1) lookup time and performs no I/O operations. All values are stored in memory.

#### Usage

```swift
let provider = InMemoryProvider(values: [
    "http.client.user-agent": "Config/1.0 (Test)",
    "http.client.timeout": 15.0,
    "http.secret": ConfigValue("s3cret", isSecret: true),
    "http.version": 2,
    "enabled": true
])
// Prints all values, redacts "http.secret" automatically.
print(provider)
let config = ConfigReader(provider: provider)
let isEnabled = config.bool(forKey: "enabled", default: false)
```

To learn more about the in-memory providers, check out [Using in-memory providers](./using-in-memory-providers.md).

## Topics

### Creating an in-memory provider
- [init(name: String?, values: [AbsoluteConfigKey : ConfigValue])](./inmemoryprovider/init%28name,values%29.md)
  Creates a new in-memory provider with the specified configuration values.
### Default Implementations
- [ConfigProvider Implementations](./inmemoryprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./inmemoryprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./inmemoryprovider/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [ConfigProvider](./configprovider.md)
- Swift.Copyable
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

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
- [Using in-memory providers](./using-in-memory-providers.md)
  Learn about the [`InMemoryProvider`](./inmemoryprovider.md) and [`MutableInMemoryProvider`](./mutableinmemoryprovider.md) built-in types.
- [class MutableInMemoryProvider](./mutableinmemoryprovider.md)
  A configuration provider that stores mutable values in memory.
- [struct KeyMappingProvider](./keymappingprovider.md)
  A configuration provider that maps all keys before delegating to an upstream provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/inmemoryprovider)*