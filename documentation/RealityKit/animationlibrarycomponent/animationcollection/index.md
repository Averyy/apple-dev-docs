# AnimationLibraryComponent.AnimationCollection.Index

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that represents a position in the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Index
```

## Topics

### Operators
- [static func < (AnimationLibraryComponent.AnimationCollection.Index, AnimationLibraryComponent.AnimationCollection.Index) -> Bool](./index/op%28_,_%29.md)
  Returns a Boolean value that indicates whether the first argument represents a position before the second argument.

## Relationships

### Conforms To
- [Comparable](../../../Swift/comparable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Manipulating indices
- [var startIndex: AnimationLibraryComponent.AnimationCollection.Index](./startindex.md)
  An index to the first animation in the collection.
- [var endIndex: AnimationLibraryComponent.AnimationCollection.Index](./endindex.md)
  An index to the last animation in the collection.
- [func index(after: AnimationLibraryComponent.AnimationCollection.Index) -> AnimationLibraryComponent.AnimationCollection.Index](./index%28after%29.md)
  Returns the position in the collection that follows an index.
- [func formIndex(after: inout AnimationLibraryComponent.AnimationCollection.Index)](./formindex%28after%29.md)
  Replaces the index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection/index)*