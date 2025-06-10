# actionEnded(event:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

The function used to respond to action ended events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
mutating func actionEnded(event: Self.EventType)
```

#### Discussion

Action ended is raised after a ‘started’ event has taken place, and the animation time exits the event interval, or when the animation is terminated before completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/actionended(event:))*