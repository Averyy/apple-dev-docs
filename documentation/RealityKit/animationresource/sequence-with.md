# sequence(with:)

**Framework**: RealityKit  
**Kind**: method

Creates an animation resource that plays a collection of animations in a specified sequence.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency static func sequence(with resources: [AnimationResource]) throws -> AnimationResource
```

#### Return Value

An animation resource that plays the given array of animations.

## Parameters

- `resources`: The collection of animation resources to play.

## See Also

- [static func generate(with: any AnimationDefinition) throws -> AnimationResource](animationresource/generate(with:).md)
  Creates an animation resource from a definition.
- [static func group(with: [AnimationResource]) throws -> AnimationResource](animationresource/group(with:).md)
  Creates an animation resource that simultaneously plays back a collection of animations.
- [func `repeat`(count: Int) -> AnimationResource](animationresource/repeat(count:).md)
  Creates an animation that repeats the specified number of times.
- [func `repeat`(duration: TimeInterval) -> AnimationResource](animationresource/repeat(duration:).md)
  Repeats an animation for the specified amount of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource/sequence(with:))*