# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the color parameter by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
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
- [static func != (Self, Self) -> Bool](materialcolorparameter/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](materialcolorparameter/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/materialcolorparameter/hash(into:))*