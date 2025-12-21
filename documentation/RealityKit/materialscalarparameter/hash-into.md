# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the scalar parameter by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the   scalar parameter.

## See Also

- [static func == (MaterialScalarParameter, MaterialScalarParameter) -> Bool](materialscalarparameter/==(_:_:).md)
  Indicates whether two scalar parameters are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialscalarparameter/hash(into:))*