---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/propertylistsnapshot"
framework: "swift-configuration/Configuration"
---

# PropertyListSnapshot

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A snapshot of configuration values parsed from property list (plist) data.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct PropertyListSnapshot
```

#### Overview

This structure represents a point-in-time view of configuration values. It handles the conversion from property list types to configuration value types.

#### Usage

Use with [`FileProvider`](./fileprovider.md) or [`ReloadingFileProvider`](./reloadingfileprovider.md):

```swift
let provider = try await FileProvider<PropertyListSnapshot>(filePath: "/etc/config.plist")
let config = ConfigReader(provider: provider)
```

## Topics

### Creating a property list snapshot
- [init(data: RawSpan, providerName: String, parsingOptions: PropertyListSnapshot.ParsingOptions) throws](./propertylistsnapshot/init%28data,providername,parsingoptions%29.md)
  Creates a new snapshot from file data.
- [PropertyListSnapshot.ParsingOptions](./propertylistsnapshot/parsingoptions.md)
  Parsing options for property list snapshot creation.
### Snapshot configuration
- [protocol FileConfigSnapshot](./fileconfigsnapshot.md)
  A protocol for configuration snapshots created from file data.
- [protocol ConfigSnapshot](./configsnapshot.md)
  An immutable snapshot of a configuration provider’s state.
### Instance Properties
- [let providerName: String](./propertylistsnapshot/providername.md)
  The name of the provider that created this snapshot.
### Default Implementations
- [ConfigSnapshot Implementations](./propertylistsnapshot/configsnapshot-implementations.md)
- [CustomDebugStringConvertible Implementations](./propertylistsnapshot/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./propertylistsnapshot/customstringconvertible-implementations.md)
- [FileConfigSnapshot Implementations](./propertylistsnapshot/fileconfigsnapshot-implementations.md)

## Relationships

### Conforms To
- [ConfigSnapshot](./configsnapshot.md)
- [FileConfigSnapshot](./fileconfigsnapshot.md)
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/propertylistsnapshot)*