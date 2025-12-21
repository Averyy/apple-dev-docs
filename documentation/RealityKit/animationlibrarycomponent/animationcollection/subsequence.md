# AnimationLibraryComponent.AnimationCollection.SubSequence

**Framework**: RealityKit  
**Kind**: typealias

A sequence that represents a contiguous subrange of animations in the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
typealias SubSequence = Slice<AnimationLibraryComponent.AnimationCollection>
```

## See Also

- [subscript(String) -> AnimationResource?](animationlibrarycomponent/animationcollection/subscript(_:)-4sfyo.md)
  Accesses a single animation in the collection with a key.
- [subscript(Range<AnimationLibraryComponent.AnimationCollection.Index>) -> AnimationLibraryComponent.AnimationCollection.SubSequence](animationlibrarycomponent/animationcollection/subscript(_:)-2n5pw.md)
  Accesses animations in the collection within an index range.
- [subscript(AnimationLibraryComponent.AnimationCollection.Index) -> AnimationLibraryComponent.AnimationCollection.Element](animationlibrarycomponent/animationcollection/subscript(_:)-45p83.md)
  Accesses a single animation in the collection at an index.
- [AnimationLibraryComponent.AnimationCollection.Element](animationlibrarycomponent/animationcollection/element.md)
  A key-value pair from the collection consisting of the name of an animation and the animation itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection/subsequence)*