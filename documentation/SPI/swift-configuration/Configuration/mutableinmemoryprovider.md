---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider"
framework: "swift-configuration/Configuration"
---

# MutableInMemoryProvider

**Framework**: swift-configuration/Configuration  
**Kind**: class  
**Role**: Class

A configuration provider that stores mutable values in memory.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
final class MutableInMemoryProvider
```

## Mentions

- [Using in-memory providers](./using-in-memory-providers.md)

#### Overview

Unlike [`InMemoryProvider`](./inmemoryprovider.md), this provider allows configuration values to be modified after initialization. It maintains thread-safe access to values and supports real-time notifications when values change, making it ideal for dynamic configuration scenarios.

#### Change notifications

The provider supports watching for configuration changes through the standard [`ConfigProvider`](./configprovider.md) watching methods. When a value changes, all active watchers are automatically notified with the new value.

#### Use cases

The mutable in-memory provider is particularly useful for:

- **Dynamic configuration**: Values that change during application runtime
- **Configuration bridges**: Adapting external configuration systems that push updates
- **Testing scenarios**: Simulating configuration changes in unit tests
- **Feature flags**: Runtime toggles that can be modified programmatically

#### Performance characteristics

This provider offers O(1) lookup time with minimal synchronization overhead. Value updates are atomic and efficiently notify only the relevant watchers.

#### Usage

```swift
// Create provider with initial values
let provider = MutableInMemoryProvider(initialValues: [
    "feature.enabled": true,
    "api.timeout": 30.0,
    "database.host": "localhost"
])

let config = ConfigReader(provider: provider)

// Read initial values
let isEnabled = config.bool(forKey: "feature.enabled") // true

// Update values dynamically
provider.setValue(false, forKey: "feature.enabled")

// Read updated values
let stillEnabled = config.bool(forKey: "feature.enabled") // false
```

To learn more about the in-memory providers, check out [Using in-memory providers](./using-in-memory-providers.md).

## Topics

### Creating a mutable in-memory provider
- [init(name: String?, initialValues: [AbsoluteConfigKey : ConfigValue])](./mutableinmemoryprovider/init%28name,initialvalues%29.md)
  Creates a new mutable in-memory provider with the specified initial values.
### Updating values in a mutable in-memory provider
- [func setValue(ConfigValue?, forKey: AbsoluteConfigKey)](./mutableinmemoryprovider/setvalue%28_,forkey%29.md)
  Updates the stored value for the specified configuration key.
### Default Implementations
- [ConfigProvider Implementations](./mutableinmemoryprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./mutableinmemoryprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./mutableinmemoryprovider/customstringconvertible-implementations.md)

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
- [struct InMemoryProvider](./inmemoryprovider.md)
  A configuration provider that stores values in memory.
- [struct KeyMappingProvider](./keymappingprovider.md)
  A configuration provider that maps all keys before delegating to an upstream provider.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/mutableinmemoryprovider)*