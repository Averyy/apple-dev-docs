# move(to:relativeTo:duration:timingFunction:)

**Framework**: RealityKit  
**Kind**: method

Moves an entity over a period of time to a new location given by a 4x4 matrix.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func move(to target: float4x4, relativeTo referenceEntity: Entity?, duration: TimeInterval, timingFunction: AnimationTimingFunction = .default) -> AnimationPlaybackController
```

#### Return Value

An [`AnimationPlaybackController`](animationplaybackcontroller.md) instance that you use to control the animation playback.

## Parameters

- `target`: A 4x4 matrix that indicates the new location.
- `referenceEntity`: The entity that defines a frame of reference. Set   this to   to indicate world space.
- `duration`: The time in seconds over which the move should occur.
- `timingFunction`: A timing function that controls the progress of the   animation.

## See Also

- [func move(to: Transform, relativeTo: Entity?, duration: TimeInterval, timingFunction: AnimationTimingFunction) -> AnimationPlaybackController](hastransform/move(to:relativeto:duration:timingfunction:)-35qp2.md)
  Moves an entity over a period of time to a new location given by a transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hastransform/move(to:relativeto:duration:timingfunction:)-6la93)*