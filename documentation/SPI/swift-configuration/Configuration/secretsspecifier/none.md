---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/none"
framework: "swift-configuration/Configuration"
---

# SecretsSpecifier.none

**Framework**: swift-configuration/Configuration  
**Kind**: case  
**Role**: Case

The library treats no configuration values as secrets.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case none
```

## Discussion

Use this case when the provider handles only non-sensitive configuration data that can be safely logged or displayed.

## See Also

### Types of specifiers
- [SecretsSpecifier.all](./all.md)
  The library treats all configuration values as secrets.
- [SecretsSpecifier.specific(_:)](./specific%28_%29.md)
  The library treats the specified keys as secrets.
- [case dynamic((KeyType, ValueType) -> Bool)](./dynamic%28_%29.md)
  The library determines the secret status dynamically by evaluating each key-value pair.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/none)*