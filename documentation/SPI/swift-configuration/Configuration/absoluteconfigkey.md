---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey"
framework: "swift-configuration/Configuration"
---

# AbsoluteConfigKey

**Framework**: swift-configuration/Configuration  
**Kind**: struct  
**Role**: Structure

A configuration key that represents an absolute path to a configuration value.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct AbsoluteConfigKey
```

## Mentions

- [Using in-memory providers](./using-in-memory-providers.md)

## Overview

Absolute configuration keys are similar to relative keys but represent complete paths from the root of the configuration hierarchy. The configuration system uses them internally after resolving key prefixes or scoping.

Like relative keys, absolute keys consist of hierarchical components and optional context information.

## Topics

### Creating an absolute configuration key
- [init(ConfigKey)](./absoluteconfigkey/init%28_%29.md)
  Creates a new absolute configuration key from a relative key.
- [init([String], context: [String : ConfigContextValue])](./absoluteconfigkey/init%28_,context%29.md)
  Creates a new absolute configuration key.
### Inspecting an absolute configuration key
- [var components: [String]](./absoluteconfigkey/components.md)
  The hierarchical components that make up this absolute configuration key.
- [var context: [String : ConfigContextValue]](./absoluteconfigkey/context.md)
  Additional context information for this configuration key.
### Instance Methods
- [func appending(ConfigKey) -> AbsoluteConfigKey](./absoluteconfigkey/appending%28_%29.md)
  Returns a new absolute configuration key by appending the given relative key.
- [func prepending(ConfigKey) -> AbsoluteConfigKey](./absoluteconfigkey/prepending%28_%29.md)
  Returns a new absolute configuration key by prepending the given relative key.
### Default Implementations
- [Comparable Implementations](./absoluteconfigkey/comparable-implementations.md)
- [CustomStringConvertible Implementations](./absoluteconfigkey/customstringconvertible-implementations.md)
- [Equatable Implementations](./absoluteconfigkey/equatable-implementations.md)
- [ExpressibleByArrayLiteral Implementations](./absoluteconfigkey/expressiblebyarrayliteral-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./absoluteconfigkey/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](./absoluteconfigkey/expressiblebystringliteral-implementations.md)

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
- [struct ConfigKey](./configkey.md)
  A configuration key representing a relative path to a configuration value.
- [enum ConfigContextValue](./configcontextvalue.md)
  A value that can be stored in a configuration context.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/absoluteconfigkey)*