# index(after:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Returns the position in the collection that follows an index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
func index(after i: AnimationLibraryComponent.AnimationCollection.Index) -> AnimationLibraryComponent.AnimationCollection.Index
```

## Parameters

- `i`: A valid index of the collection. `i` must be less than `endIndex`.

## See Also

### Manipulating indices
- [var startIndex: AnimationLibraryComponent.AnimationCollection.Index](./startindex.md)
  An index to the first animation in the collection.
- [var endIndex: AnimationLibraryComponent.AnimationCollection.Index](./endindex.md)
  An index to the last animation in the collection.
- [func formIndex(after: inout AnimationLibraryComponent.AnimationCollection.Index)](./formindex%28after%29.md)
  Replaces the index with its successor.
- [AnimationLibraryComponent.AnimationCollection.Index](./index.md)
  An object that represents a position in the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection/index(after:))*