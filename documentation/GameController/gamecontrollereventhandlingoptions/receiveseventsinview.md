# receivesEventsInView(_:)

**Framework**: Game Controller  
**Kind**: method

A Boolean option that determines whether events are delivered exclusively through the GameController framework.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
static func receivesEventsInView(_ receivesEventsInView: Bool) -> GameControllerEventHandlingOptions
```

#### Discussion

If `true`, events are delivered both through the Game Controller framework and as SwiftUI events to your app’s views and gesture recognizers.

If `false`, events are delivered  through the Game Controller framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gamecontrollereventhandlingoptions/receiveseventsinview(_:))*