# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the shape by feeding them into the given hash function.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher`: The hash function to use when combining the components of the   shape.

## See Also

- [static func == (ShapeResource, ShapeResource) -> Bool](shaperesource/==(_:_:).md)
  Indicates whether two shapes are equal.
- [static func != (Self, Self) -> Bool](shaperesource/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](shaperesource/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shaperesource/hash(into:))*