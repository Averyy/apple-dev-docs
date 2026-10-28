# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses a single animation in the collection at an index.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
subscript(position: AnimationLibraryComponent.AnimationCollection.Index) -> AnimationLibraryComponent.AnimationCollection.Element { get }
```

**Other overloads**:

```swift
subscript(bounds: Range<AnimationLibraryComponent.AnimationCollection.Index>) -> AnimationLibraryComponent.AnimationCollection.SubSequence { get }
```

```swift
subscript(key: String) -> AnimationResource? { get set }
```

## Return Value

The animation at the dictionary index.

## Parameters

- `position`: An index into the collection’s dictionary.

## See Also

### Accessing animations
- [subscript(String) -> AnimationResource?](./subscript%28_%29-4sfyo.md)
  Accesses a single animation in the collection with a key.
- [subscript(Range<AnimationLibraryComponent.AnimationCollection.Index>) -> AnimationLibraryComponent.AnimationCollection.SubSequence](./subscript%28_%29-2n5pw.md)
  Accesses animations in the collection within an index range.
- [AnimationLibraryComponent.AnimationCollection.SubSequence](./subsequence.md)
  A sequence that represents a contiguous subrange of animations in the collection.
- [AnimationLibraryComponent.AnimationCollection.Element](./element.md)
  A key-value pair from the collection consisting of the name of an animation and the animation itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection/subscript(_:)-45p83)*