# startIndex

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The position of the first element in a nonempty collection.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency var startIndex: Int { get }
```

#### Discussion

If the collection is empty, `startIndex` is equal to `endIndex`.

## See Also

### Manipulating indices
- [Scene.AnchorCollection.Index](./index.md)
  A type that represents a position in the collection.
- [var endIndex: Int](./endindex.md)
  The position one greater than the last valid subscript argument.
- [func index(after: Int) -> Int](./index%28after%29.md)
  Returns the position immediately after the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/anchorcollection/startindex)*