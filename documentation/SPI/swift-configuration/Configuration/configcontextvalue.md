---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configcontextvalue"
framework: "swift-configuration/Configuration"
---

# ConfigContextValue

**Framework**: swift-configuration/Configuration  
**Kind**: enum  
**Role**: Enumeration

A value that can be stored in a configuration context.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
enum ConfigContextValue
```

## Overview

Context values support common data types for configuration metadata.

## Topics

### Configuration context values
- [ConfigContextValue.string(_:)](./configcontextvalue/string%28_%29.md)
  A string value.
- [ConfigContextValue.bool(_:)](./configcontextvalue/bool%28_%29.md)
  A Boolean value.
- [ConfigContextValue.int(_:)](./configcontextvalue/int%28_%29.md)
  An integer value.
- [ConfigContextValue.double(_:)](./configcontextvalue/double%28_%29.md)
  A floating point value.
### Default Implementations
- [CustomStringConvertible Implementations](./configcontextvalue/customstringconvertible-implementations.md)
- [Equatable Implementations](./configcontextvalue/equatable-implementations.md)
- [ExpressibleByBooleanLiteral Implementations](./configcontextvalue/expressiblebybooleanliteral-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./configcontextvalue/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByFloatLiteral Implementations](./configcontextvalue/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./configcontextvalue/expressiblebyintegerliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](./configcontextvalue/expressiblebystringliteral-implementations.md)

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

### Configuration keys
- [struct ConfigKey](./configkey.md)
  A configuration key representing a relative path to a configuration value.
- [struct AbsoluteConfigKey](./absoluteconfigkey.md)
  A configuration key that represents an absolute path to a configuration value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configcontextvalue)*