# index(after:)

**Framework**: RealityKit  
**Kind**: method

Returns the position immediately after the given index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func index(after i: Int) -> Int
```

#### Return Value

The index value immediately after i.

## Parameters

- `i`: A valid index of the collection. Use a value less than  .

## See Also

- [Scene.AnchorCollection.Index](scene/anchorcollection/index.md)
  A type that represents a position in the collection.
- [Scene.AnchorCollection.Indices](scene/anchorcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [var startIndex: Int](scene/anchorcollection/startindex.md)
  The position of the first element in a nonempty collection.
- [var endIndex: Int](scene/anchorcollection/endindex.md)
  The position one greater than the last valid subscript argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/index(after:))*