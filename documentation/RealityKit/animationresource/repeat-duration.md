# repeat(duration:)

**Framework**: RealityKit  
**Kind**: method

Repeats an animation for the specified amount of time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func `repeat`(duration: TimeInterval = .infinity) -> AnimationResource
```

#### Return Value

A new animation resource that you play on an entity by calling the entity’s [`playAnimation(_:transitionDuration:startsPaused:)`](entity/playanimation(_:transitionduration:startspaused:).md) method.

## Parameters

- `duration`: The amount of time that the animation should play. If you   omit this parameter, the animation loops indefinitely.

## See Also

- [static generate(with:)](animationresource/generate(with:).md)
  Creates an animation resource from a definition.
- [static sequence(with:)](animationresource/sequence(with:).md)
  Creates an animation resource that plays a collection of animations in a specified sequence.
- [static group(with:)](animationresource/group(with:).md)
  Creates an animation resource that simultaneously plays back a collection of animations.
- [func `repeat`(count: Int) -> AnimationResource](animationresource/repeat(count:).md)
  Creates an animation that repeats the specified number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource/repeat(duration:))*