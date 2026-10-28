---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configvalue"
framework: "swift-configuration/Configuration"
---

# ConfigValue

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration value that wraps content with metadata.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfigValue
```

## Mentions

- [Handling secrets correctly](./handling-secrets-correctly.md)

## Overview

Configuration values pair raw content with a flag indicating whether the value contains sensitive information. Secret values are protected from accidental disclosure in logs and debug output:

```swift
let apiKey = ConfigValue(.string("sk-abc123"), isSecret: true)
print(apiKey)  // Prints: [string: <REDACTED>]
```

## Topics

### Creating a config value
- [init(ConfigContent, isSecret: Bool)](./configvalue/init%28_,issecret%29.md)
  Creates a new configuration value.
### Inspecting a config value
- [var content: ConfigContent](./configvalue/content.md)
  The configuration content.
- [var isSecret: Bool](./configvalue/issecret.md)
  Whether this value contains sensitive information that should not be logged.
### Default Implementations
- [CustomStringConvertible Implementations](./configvalue/customstringconvertible-implementations.md)
- [Equatable Implementations](./configvalue/equatable-implementations.md)
- [ExpressibleByBooleanLiteral Implementations](./configvalue/expressiblebybooleanliteral-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./configvalue/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByFloatLiteral Implementations](./configvalue/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./configvalue/expressiblebyintegerliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](./configvalue/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
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
- [enum ConfigContent](./configcontent.md)
  The raw content of a configuration value.
- [enum ConfigType](./configtype.md)
  The supported configuration value types.
- [struct LookupResult](./lookupresult.md)
  The result of looking up a configuration value in a provider.
- [enum SecretsSpecifier](./secretsspecifier.md)
  A specification for identifying which configuration values contain sensitive information.
- [struct ConfigUpdatesAsyncSequence](./configupdatesasyncsequence.md)
  A concrete async sequence for delivering updated configuration values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configvalue)*