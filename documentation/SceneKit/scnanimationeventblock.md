# SCNAnimationEventBlock

**Framework**: SceneKit  
**Kind**: typealias

Signature for the block called when an animation event triggers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
typealias SCNAnimationEventBlock = (any SCNAnimationProtocol, Any, Bool) -> Void
```

#### Discussion

The block takes the following parameters:

- **animation**: The animation triggering the animation event.
- **animatedObject**: The Scene Kit object affected by the animation.
- **playingBackward**: [`true`](https://developer.apple.com/documentation/swift/true) if the animation is playing in reverse; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimationeventblock)*