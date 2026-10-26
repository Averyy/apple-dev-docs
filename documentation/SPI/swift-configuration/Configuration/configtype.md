---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configtype"
framework: "swift-configuration/Configuration"
---

# ConfigType

**Framework**: swift-configuration/Configuration  
**Kind**: enum  
**Role**: Enumeration

The supported configuration value types.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
enum ConfigType
```

## Topics

### Types of configuration content
- [ConfigType.string](./configtype/string.md)
  A string value.
- [ConfigType.stringArray](./configtype/stringarray.md)
  An array of string values.
- [ConfigType.bool](./configtype/bool.md)
  A Boolean value.
- [ConfigType.boolArray](./configtype/boolarray.md)
  An array of Boolean values.
- [ConfigType.int](./configtype/int.md)
  An integer value.
- [ConfigType.intArray](./configtype/intarray.md)
  An array of integer values.
- [ConfigType.double](./configtype/double.md)
  A double value.
- [ConfigType.doubleArray](./configtype/doublearray.md)
  An array of double values.
- [ConfigType.bytes](./configtype/bytes.md)
  An array of bytes.
- [ConfigType.byteChunkArray](./configtype/bytechunkarray.md)
  An array of byte chunks.
### Initializers
- [init?(rawValue: String)](./configtype/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./configtype/equatable-implementations.md)
- [RawRepresentable Implementations](./configtype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.BitwiseCopyable
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

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
- [struct LookupResult](./lookupresult.md)
  The result of looking up a configuration value in a provider.
- [enum SecretsSpecifier](./secretsspecifier.md)
  A specification for identifying which configuration values contain sensitive information.
- [struct ConfigUpdatesAsyncSequence](./configupdatesasyncsequence.md)
  A concrete async sequence for delivering updated configuration values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configtype)*