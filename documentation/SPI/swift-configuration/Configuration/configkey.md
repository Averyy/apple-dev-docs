---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configkey"
framework: "swift-configuration/Configuration"
---

# ConfigKey

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration key representing a relative path to a configuration value.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ConfigKey
```

## Overview

Configuration keys consist of hierarchical string components forming paths similar to file system paths or JSON object keys. For example, `["http", "timeout"]` represents the `timeout` value nested under `http`.

Keys support additional context information that providers can use to refine lookups or provide specialized behavior.

## Usage

Create keys using string literals, arrays, or the initializers:

```swift
let key1: ConfigKey = "database.connection.timeout"
let key2 = ConfigKey(["api", "endpoints", "primary"])
let key3 = ConfigKey("server.port", context: ["environment": .string("production")])
```

## Topics

### Creating a configuration key
- [init(String, context: [String : ConfigContextValue])](./configkey/init%28_,context%29-6vten.md)
  Creates a new configuration key.
- [init([String], context: [String : ConfigContextValue])](./configkey/init%28_,context%29-9ifez.md)
  Creates a new configuration key.
### Inspecting a configuration key
- [var components: [String]](./configkey/components.md)
  The hierarchical components that make up this configuration key.
- [var context: [String : ConfigContextValue]](./configkey/context.md)
  Additional context information for this configuration key.
### Default Implementations
- [Comparable Implementations](./configkey/comparable-implementations.md)
- [CustomStringConvertible Implementations](./configkey/customstringconvertible-implementations.md)
- [Equatable Implementations](./configkey/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](./configkey/expressiblebyarrayliteral-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./configkey/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](./configkey/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- Swift.Comparable
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Escapable
- Swift.ExpressibleByArrayLiteral
- Swift.ExpressibleByExtendedGraphemeClusterLiteral
- Swift.ExpressibleByStringLiteral
- Swift.ExpressibleByUnicodeScalarLiteral
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Configuration keys
- [struct AbsoluteConfigKey](./absoluteconfigkey.md)
  A configuration key that represents an absolute path to a configuration value.
- [enum ConfigContextValue](./configcontextvalue.md)
  A value that can be stored in a configuration context.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/configkey)*