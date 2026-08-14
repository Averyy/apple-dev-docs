# AnimationLibraryComponent.AnimationCollection.Index

**Framework**: RealityKit  
**Kind**: struct

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
- [static func < (AnimationLibraryComponent.AnimationCollection.Index, AnimationLibraryComponent.AnimationCollection.Index) -> Bool](animationlibrarycomponent/animationcollection/index/_(_:_:).md)
  Returns a Boolean value that indicates whether the first argument represents a position before the second argument.

## Relationships

### Conforms To
- [Comparable](../swift/comparable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var startIndex: AnimationLibraryComponent.AnimationCollection.Index](animationlibrarycomponent/animationcollection/startindex.md)
  An index to the first animation in the collection.
- [var endIndex: AnimationLibraryComponent.AnimationCollection.Index](animationlibrarycomponent/animationcollection/endindex.md)
  An index to the last animation in the collection.
- [func index(after: AnimationLibraryComponent.AnimationCollection.Index) -> AnimationLibraryComponent.AnimationCollection.Index](animationlibrarycomponent/animationcollection/index(after:).md)
  Returns the position in the collection that follows an index.
- [func formIndex(after: inout AnimationLibraryComponent.AnimationCollection.Index)](animationlibrarycomponent/animationcollection/formindex(after:).md)
  Replaces the index with its successor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection/index)*