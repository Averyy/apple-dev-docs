---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/lookupresult"
framework: "swift-configuration/Configuration"
---

# LookupResult

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

The result of looking up a configuration value in a provider.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct LookupResult
```

## Overview

Providers return this result from value lookup methods, containing both the encoded key used for the lookup and the value found:

```swift
let result = try provider.value(forKey: key, type: .string)
if let value = result.value {
    print("Found: \(value)")
}
```

## Topics

### Creating a lookup result
- [init(encodedKey: String, value: ConfigValue?)](./lookupresult/init%28encodedkey,value%29.md)
  Creates a lookup result.
### Inspecting a lookup result
- [var encodedKey: String](./lookupresult/encodedkey.md)
  The provider-specific encoding of the configuration key.
- [var value: ConfigValue?](./lookupresult/value.md)
  The configuration value found for the key, or nil if not found.
### Default Implementations
- [Equatable Implementations](./lookupresult/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
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
- [enum ConfigContent](./configcontent.md)
  The raw content of a configuration value.
- [struct ConfigValue](./configvalue.md)
  A configuration value that wraps content with metadata.
- [enum ConfigType](./configtype.md)
  The supported configuration value types.
- [enum SecretsSpecifier](./secretsspecifier.md)
  A specification for identifying which configuration values contain sensitive information.
- [struct ConfigUpdatesAsyncSequence](./configupdatesasyncsequence.md)
  A concrete async sequence for delivering updated configuration values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/lookupresult)*