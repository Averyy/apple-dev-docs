# AnimationLibraryComponent.AnimationCollection

**Framework**: RealityKit  
**Kind**: struct

A collection of animations an entity can play.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct AnimationCollection
```

#### Overview

You use `AnimationCollection` to access animations in an [`AnimationLibraryComponent`](animationlibrarycomponent.md).

The initializers for [`AnimationLibraryComponent`](animationlibrarycomponent.md) create an `AnimationCollection`, so you don’t need to create one directly. You can access the collection with the [`animations`](animationlibrarycomponent/animations.md) property.

## Topics

### Creating an animation collection
- [init(dictionaryLiteral: (String, AnimationResource)...)](animationlibrarycomponent/animationcollection/init(dictionaryliteral:).md)
  Creates an animation collection from a dictionary literal.
### Inspecting an animation collection
- [var count: Int](animationlibrarycomponent/animationcollection/count.md)
  The number of animations in the collection.
- [var isEmpty: Bool](animationlibrarycomponent/animationcollection/isempty.md)
  A Boolean value that indicates whether the collection is empty.
### Accessing animations
- [subscript(String) -> AnimationResource?](animationlibrarycomponent/animationcollection/subscript(_:)-4sfyo.md)
  Accesses a single animation in the collection with a key.
- [subscript(Range<AnimationLibraryComponent.AnimationCollection.Index>) -> AnimationLibraryComponent.AnimationCollection.SubSequence](animationlibrarycomponent/animationcollection/subscript(_:)-2n5pw.md)
  Accesses animations in the collection within an index range.
- [subscript(AnimationLibraryComponent.AnimationCollection.Index) -> AnimationLibraryComponent.AnimationCollection.Element](animationlibrarycomponent/animationcollection/subscript(_:)-45p83.md)
  Accesses a single animation in the collection at an index.
- [AnimationLibraryComponent.AnimationCollection.SubSequence](animationlibrarycomponent/animationcollection/subsequence.md)
  A sequence that represents a contiguous subrange of animations in the collection.
- [AnimationLibraryComponent.AnimationCollection.Element](animationlibrarycomponent/animationcollection/element.md)
  A key-value pair from the collection consisting of the name of an animation and the animation itself.
### Manipulating indices
- [var startIndex: AnimationLibraryComponent.AnimationCollection.Index](animationlibrarycomponent/animationcollection/startindex.md)
  An index to the first animation in the collection.
- [var endIndex: AnimationLibraryComponent.AnimationCollection.Index](animationlibrarycomponent/animationcollection/endindex.md)
  An index to the last animation in the collection.
- [func index(after: AnimationLibraryComponent.AnimationCollection.Index) -> AnimationLibraryComponent.AnimationCollection.Index](animationlibrarycomponent/animationcollection/index(after:).md)
  Returns the position in the collection that follows an index.
- [func formIndex(after: inout AnimationLibraryComponent.AnimationCollection.Index)](animationlibrarycomponent/animationcollection/formindex(after:).md)
  Replaces the index with its successor.
- [AnimationLibraryComponent.AnimationCollection.Index](animationlibrarycomponent/animationcollection/index.md)
  An object that represents a position in the collection.
### Iterating over animations
- [func makeIterator() -> AnimationLibraryComponent.AnimationCollection.Iterator](animationlibrarycomponent/animationcollection/makeiterator.md)
  Returns an iterator over the animations in the collection.
- [AnimationLibraryComponent.AnimationCollection.Iterator](animationlibrarycomponent/animationcollection/iterator.md)
  An object to iterate over all animations in the collection.
### Subscripts
- [subscript(_:)](animationlibrarycomponent/animationcollection/subscript(_:).md)
  Accesses animations in the collection within an index range.

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [class AnimationResource](animationresource.md)
  An animation for the properties of scenes or entities.
- [struct AnimationLibraryComponent](animationlibrarycomponent.md)
  A component that represents a collection of animations that an entity can play.
- [enum AnimationEvents](animationevents.md)
  Notable milestones that the framework signals during animation playback.
- [class AnimationPlaybackController](animationplaybackcontroller.md)
  A controller that manages animation playback.
- [enum AnimationRepeatMode](animationrepeatmode.md)
  Options that determine whether an animation replays after completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection)*