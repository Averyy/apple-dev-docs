# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the color parameter by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the   color parameter.

## See Also

- [static func == (MaterialColorParameter, MaterialColorParameter) -> Bool](materialcolorparameter/==(_:_:).md)
  Indicates whether two color parameters are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialcolorparameter/hash(into:))*