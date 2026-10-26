---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/dynamic(_:)"
framework: "swift-configuration/Configuration"
---

# SecretsSpecifier.dynamic(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: case  
**Role**: Case

The library determines the secret status dynamically by evaluating each key-value pair.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case dynamic(@Sendable (KeyType, ValueType) -> Bool)
```

#### Discussion

Use this case when you need complex logic to determine whether a value is secret based on the key name, value content, or other criteria.

## Parameters

- `closure`: A closure that takes a key and value and returns whether the value should be treated as secret.

## See Also

### Types of specifiers
- [SecretsSpecifier.all](./all.md)
  The library treats all configuration values as secrets.
- [SecretsSpecifier.specific(_:)](./specific%28_%29.md)
  The library treats the specified keys as secrets.
- [SecretsSpecifier.none](./none.md)
  The library treats no configuration values as secrets.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/dynamic(_:))*