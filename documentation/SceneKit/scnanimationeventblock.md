# SCNAnimationEventBlock

**Framework**: SceneKit  
**Kind**: typealias  
**Role**: Type Alias

Signature for the block called when an animation event triggers.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
typealias SCNAnimationEventBlock = (any SCNAnimationProtocol, Any, Bool) -> Void
```

```c
typedef void (^)(id<SCNAnimation>, id, _Bool) SCNAnimationEventBlock;
```

## Discussion

The block takes the following parameters:

- **animation**: The animation triggering the animation event.
- **animatedObject**: The Scene Kit object affected by the animation.
- **playingBackward**: [`true`](../Swift/true.md) if the animation is playing in reverse; otherwise, [`false`](../Swift/false.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnanimationeventblock)*