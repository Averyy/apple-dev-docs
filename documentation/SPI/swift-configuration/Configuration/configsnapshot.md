---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshot"
framework: "swift-configuration/Configuration"
---

# ConfigSnapshot

**Framework**: swift-configuration/Configuration  
**Kind**: protocol  
**Role**: Protocol

An immutable snapshot of a configuration provider’s state.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol ConfigSnapshot : Sendable
```

## Mentions

- [Implementing a custom provider](./implementing-a-provider.md)

#### Overview

Snapshots enable consistent reads of multiple related configuration keys by capturing the provider’s state at a specific moment. This prevents the underlying data from changing between individual key lookups.

## Topics

### Required methods
- [var providerName: String](./configsnapshot/providername.md)
  The human-readable name of the configuration provider that created this snapshot.
- [func value(forKey: AbsoluteConfigKey, type: ConfigType) throws -> LookupResult](./configsnapshot/value%28forkey,type%29.md)
  Returns a value for the specified key from this immutable snapshot.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Inherited By
- [FileConfigSnapshot](./fileconfigsnapshot.md)
### Conforming Types
- [JSONSnapshot](./jsonsnapshot.md)
- [PropertyListSnapshot](./propertylistsnapshot.md)
- [YAMLSnapshot](./yamlsnapshot.md)

## See Also

### Creating a custom provider
- [Implementing a custom provider](./implementing-a-provider.md)
  Create a custom configuration provider to integrate a new data source.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configsnapshot)*