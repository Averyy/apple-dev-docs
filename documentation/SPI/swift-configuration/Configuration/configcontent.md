---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configcontent"
framework: "swift-configuration/Configuration"
---

# ConfigContent

**Framework**: swift-configuration/Configuration  
**Kind**: enum  
**Role**: Enumeration

The raw content of a configuration value.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
enum ConfigContent
```

## Topics

### Types of configuration content
- [ConfigContent.string(_:)](./configcontent/string%28_%29.md)
  A string value.
- [ConfigContent.stringArray(_:)](./configcontent/stringarray%28_%29.md)
  An array of string values.
- [ConfigContent.bool(_:)](./configcontent/bool%28_%29.md)
  A Boolean value.
- [ConfigContent.boolArray(_:)](./configcontent/boolarray%28_%29.md)
  An array of Boolean value.
- [ConfigContent.int(_:)](./configcontent/int%28_%29.md)
  An integer value.
- [ConfigContent.intArray(_:)](./configcontent/intarray%28_%29.md)
  An array of integer values.
- [ConfigContent.double(_:)](./configcontent/double%28_%29.md)
  A double value.
- [ConfigContent.doubleArray(_:)](./configcontent/doublearray%28_%29.md)
  An array of double values.
- [ConfigContent.bytes(_:)](./configcontent/bytes%28_%29.md)
  An array of bytes.
- [ConfigContent.byteChunkArray(_:)](./configcontent/bytechunkarray%28_%29.md)
  An array of byte arrays.
### Default Implementations
- [Equatable Implementations](./configcontent/equatable-implementations.md)
- [ExpressibleByBooleanLiteral Implementations](./configcontent/expressiblebybooleanliteral-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./configcontent/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByFloatLiteral Implementations](./configcontent/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./configcontent/expressiblebyintegerliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](./configcontent/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Equatable
- Swift.Escapable
- Swift.ExpressibleByBooleanLiteral
- Swift.ExpressibleByExtendedGraphemeClusterLiteral
- Swift.ExpressibleByFloatLiteral
- Swift.ExpressibleByIntegerLiteral
- Swift.ExpressibleByStringLiteral
- Swift.ExpressibleByUnicodeScalarLiteral
- Swift.Hashable
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

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configcontent)*