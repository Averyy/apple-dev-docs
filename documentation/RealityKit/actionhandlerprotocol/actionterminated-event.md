# actionTerminated(event:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

The function used to respond to action terminated events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
mutating func actionTerminated(event: Self.EventType)
```

#### Discussion

Action terminated is raised when playback is terminated and the animation is removed from the animation system. This can occur before the animation has a chance to complete if the user manually stops the animation by calling [`stop()`](animationplaybackcontroller/stop().md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/actionterminated(event:))*