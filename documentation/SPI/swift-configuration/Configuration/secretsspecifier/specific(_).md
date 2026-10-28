---
url: "https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/specific(_:)"
framework: "swift-configuration/Configuration"
---

# SecretsSpecifier.specific(_:)

**Framework**: swift-configuration/Configuration  
**Kind**: case  
**Role**: Case

The library treats the specified keys as secrets.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
case specific(Set<KeyType>)
```

## Discussion

Use this case when you have a known set of keys that contain sensitive information. All other keys will be treated as non-secret.

## Parameters

- `keys`: The set of keys that should be treated as secrets.

## See Also

### Types of specifiers
- [SecretsSpecifier.all](./all.md)
  The library treats all configuration values as secrets.
- [case dynamic((KeyType, ValueType) -> Bool)](./dynamic%28_%29.md)
  The library determines the secret status dynamically by evaluating each key-value pair.
- [SecretsSpecifier.none](./none.md)
  The library treats no configuration values as secrets.


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-configuration/main/documentation/configuration/secretsspecifier/specific(_:))*