# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Accesses animations in the collection within an index range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
subscript(bounds: Range<AnimationLibraryComponent.AnimationCollection.Index>) -> AnimationLibraryComponent.AnimationCollection.SubSequence { get }
```

#### Return Value

A subsequence of animation resources in the range of `bounds`.

## Parameters

- `bounds`: A range of indices to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationlibrarycomponent/animationcollection/subscript(_:))*