# AnimationLibraryComponent.AnimationCollection.Index

**Framework**: RealityKit  
**Kind**: struct

An object that represents a position in the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Index
```

## Topics

### Operators
- [static func == (AnimationLibraryComponent.AnimationCollection.Index, AnimationLibraryComponent.AnimationCollection.Index) -> Bool](animationlibrarycomponent/animationcollection/index/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (AnimationLibraryComponent.AnimationCollection.Index, AnimationLibraryComponent.AnimationCollection.Index) -> Bool](animationlibrarycomponent/animationcollection/index/_(_:_:).md)
  Returns a Boolean value that indicates whether the first argument represents a position before the second argument.
### Instance Properties
- [var hashValue: Int](animationlibrarycomponent/animationcollection/index/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](animationlibrarycomponent/animationcollection/index/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Comparable Implementations](animationlibrarycomponent/animationcollection/index/comparable-implementations.md)
- [Equatable Implementations](animationlibrarycomponent/animationcollection/index/equatable-implementations.md)

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

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