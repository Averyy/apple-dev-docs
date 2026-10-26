---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileconfigsnapshot"
framework: "swift-configuration/Configuration"
---

# FileConfigSnapshot

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

A protocol for configuration snapshots created from file data.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol FileConfigSnapshot : ConfigSnapshot, CustomDebugStringConvertible, CustomStringConvertible
```

## Mentions

- [Implementing a custom provider](./implementing-a-provider.md)

#### Overview

This protocol extends [`ConfigSnapshot`](./configsnapshot.md) to provide file-specific functionality for creating configuration snapshots from raw file data. Types conforming to this protocol can parse various file formats (such as JSON and YAML) and convert them into configuration values.

Commonly used with [`FileProvider`](./fileprovider.md) and [`ReloadingFileProvider`](./reloadingfileprovider.md).

#### Implementation

To create a custom file configuration snapshot:

```swift
struct MyFormatSnapshot: FileConfigSnapshot {
    typealias ParsingOptions = MyParsingOptions

    let values: [String: ConfigValue]
    let providerName: String

    init(data: RawSpan, providerName: String, parsingOptions: MyParsingOptions) throws {
        self.providerName = providerName
        // Parse the data according to your format
        self.values = try parseMyFormat(data, using: parsingOptions)
    }
}
```

The snapshot is responsible for parsing the file data and converting it into a representation of configuration values that can be queried by the configuration system.

## Topics

### Required methods
- [init(data: RawSpan, providerName: String, parsingOptions: Self.ParsingOptions) throws](./fileconfigsnapshot/init%28data,providername,parsingoptions%29.md)
  Creates a new snapshot from file data.
- [associatedtype ParsingOptions : FileParsingOptions](./fileconfigsnapshot/parsingoptions.md)
  The parsing options type used for parsing this snapshot.
### Protocol requirements
- [protocol ConfigSnapshot](./configsnapshot.md)
  An immutable snapshot of a configuration provider’s state.

## Relationships

### Inherits From
- [ConfigSnapshot](./configsnapshot.md)
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [JSONSnapshot](./jsonsnapshot.md)
- [PropertyListSnapshot](./propertylistsnapshot.md)
- [YAMLSnapshot](./yamlsnapshot.md)

## See Also

### Creating a custom provider
- [Implementing a custom provider](./implementing-a-provider.md)
  Create a custom configuration provider to integrate a new data source.
- [protocol ConfigSnapshot](./configsnapshot.md)
  An immutable snapshot of a configuration provider’s state.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/fileconfigsnapshot)*