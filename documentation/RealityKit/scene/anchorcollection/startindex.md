# startIndex

**Framework**: RealityKit  
**Kind**: property

The position of the first element in a nonempty collection.

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
@preconcurrency var startIndex: Int { get }
```

#### Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.

## See Also

- [Scene.AnchorCollection.Index](scene/anchorcollection/index.md)
  A type that represents a position in the collection.
- [Scene.AnchorCollection.Indices](scene/anchorcollection/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [var endIndex: Int](scene/anchorcollection/endindex.md)
  The position one greater than the last valid subscript argument.
- [func index(after: Int) -> Int](scene/anchorcollection/index(after:).md)
  Returns the position immediately after the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/startindex)*