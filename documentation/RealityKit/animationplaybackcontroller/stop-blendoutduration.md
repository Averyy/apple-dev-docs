# stop(blendOutDuration:)

**Framework**: RealityKit  
**Kind**: method

Stops an animation with a fade-out time.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func stop(blendOutDuration: TimeInterval)
```

#### Discussion

This method has no effect if the animation is complete. After you stop the animation, the playback controller becomes invalid. Create a new one with the same resource to play the animation again.

## Parameters

- `blendOutDuration`: Time (in seconds) to fade out the animation before it stops.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationplaybackcontroller/stop(blendoutduration:))*