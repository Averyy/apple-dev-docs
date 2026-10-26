---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence"
framework: "swift-configuration/Configuration"
---

# ConfigUpdatesAsyncSequence

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A concrete async sequence for delivering updated configuration values.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfigUpdatesAsyncSequence<Element, Failure> where Element : Sendable, Failure : Error
```

## Topics

### Creating an asynchronous update sequence
- [init(some Sendable & AsyncSequence<Element, Failure>)](./configupdatesasyncsequence/init%28_%29.md)
  Creates a new concrete async sequence wrapping the provided existential sequence.
### Default Implementations
- [AsyncSequence Implementations](./configupdatesasyncsequence/asyncsequence-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.AsyncSequence

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
- [enum ConfigType](./configtype.md)
  The supported configuration value types.
- [struct LookupResult](./lookupresult.md)
  The result of looking up a configuration value in a provider.
- [enum SecretsSpecifier](./secretsspecifier.md)
  A specification for identifying which configuration values contain sensitive information.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configupdatesasyncsequence)*