# hash(into:)

**Framework**: RealityKit  
**Kind**: method

Hashes the essential components of the bounding box by feeding them into the given hash function.

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

- `hasher`: The hash function to use when combining the components of the   box.

## See Also

- [static func == (BoundingBox, BoundingBox) -> Bool](boundingbox/==(_:_:).md)
  Indicates whether two bounding boxes are equal.
- [static func != (Self, Self) -> Bool](boundingbox/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [var hashValue: Int](boundingbox/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/boundingbox/hash(into:))*