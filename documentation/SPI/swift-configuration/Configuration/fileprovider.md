---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider"
framework: "swift-configuration/Configuration"
---

# FileProvider

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration provider that reads from a file on disk using a configurable snapshot type.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct FileProvider<Snapshot> where Snapshot : FileConfigSnapshot
```

## Mentions

- [Implementing a custom provider](./implementing-a-provider.md)
- [Example use cases](./example-use-cases.md)
- [Troubleshooting and access reporting](./troubleshooting.md)

## Overview

`FileProvider` is a generic file-based configuration provider that works with different file formats by using different snapshot types that conform to [`FileConfigSnapshot`](./fileconfigsnapshot.md). This allows for a unified interface for reading JSON, YAML, or other structured configuration files.

## Usage

Create a provider by specifying the snapshot type and file path:

```swift
// Using with a JSON snapshot
let jsonProvider = try await FileProvider<JSONSnapshot>(
    filePath: "/etc/config.json"
)

// Using with a YAML snapshot
let yamlProvider = try await FileProvider<YAMLSnapshot>(
    filePath: "/etc/config.yaml"
)
```

The provider reads the file once during initialization and creates an immutable snapshot of the configuration values. For auto-reloading behavior, use [`ReloadingFileProvider`](./reloadingfileprovider.md).

## Configuration from a reader

You can also initialize the provider using a configuration reader that specifies the file path through environment variables or other configuration sources:

```swift
let envConfig = ConfigReader(provider: EnvironmentVariablesProvider())
let provider = try await FileProvider<JSONSnapshot>(config: envConfig)
```

This expects a `filePath` key in the configuration that specifies the path to the file. For a full list of configuration keys, check out [`init(snapshotType:parsingOptions:config:)`](./fileprovider/init%28snapshottype,parsingoptions,config%29.md).

## Topics

### Creating a file provider
- [init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, filePath: FilePath, allowMissing: Bool) async throws](./fileprovider/init%28snapshottype,parsingoptions,filepath,allowmissing%29.md)
  Creates a file provider that reads from the specified file path.
- [init(snapshotType: Snapshot.Type, parsingOptions: Snapshot.ParsingOptions, config: ConfigReader) async throws](./fileprovider/init%28snapshottype,parsingoptions,config%29.md)
  Creates a file provider using a file path from a configuration reader.
### Reading configuration files
- [protocol FileConfigSnapshot](./fileconfigsnapshot.md)
  A protocol for configuration snapshots created from file data.
- [struct JSONSnapshot](./jsonsnapshot.md)
  A snapshot of configuration values parsed from JSON data.
- [class YAMLSnapshot](./yamlsnapshot.md)
  A snapshot of configuration values parsed from YAML data.
- [struct PropertyListSnapshot](./propertylistsnapshot.md)
  A snapshot of configuration values parsed from property list (plist) data.
### Default Implementations
- [ConfigProvider Implementations](./fileprovider/configprovider-implementations.md)
- [CustomDebugStringConvertible Implementations](./fileprovider/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./fileprovider/customstringconvertible-implementations.md)

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


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileprovider)*