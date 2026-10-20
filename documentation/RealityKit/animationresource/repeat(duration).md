# repeat(duration:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Repeats an animation for the specified amount of time.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func `repeat`(duration: TimeInterval = .infinity) -> AnimationResource
```

#### Return Value

A new animation resource that you play on an entity by calling the entity’s [`playAnimation(_:transitionDuration:startsPaused:)`](../entity/playanimation%28_,transitionduration,startspaused%29.md) method.

## Parameters

- `duration`: The amount of time that the animation should play. If you omit this parameter, the animation loops indefinitely.

## See Also

### Creating an animation resource
- [static func generate(with: any AnimationDefinition) throws -> AnimationResource](./generate%28with%29.md)
  Creates an animation resource from a definition.
- [static func sequence(with: [AnimationResource]) throws -> AnimationResource](./sequence%28with%29.md)
  Creates an animation resource that plays a collection of animations in a specified sequence.
- [static func group(with: [AnimationResource]) throws -> AnimationResource](./group%28with%29.md)
  Creates an animation resource that simultaneously plays back a collection of animations.
- [func `repeat`(count: Int) -> AnimationResource](./repeat%28count%29.md)
  Creates an animation that repeats the specified number of times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationresource/repeat(duration:))*