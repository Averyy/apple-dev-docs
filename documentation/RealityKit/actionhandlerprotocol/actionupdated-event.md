# actionUpdated(event:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

The function used to respond to action updated events.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
mutating func actionUpdated(event: Self.EventType)
```

#### Discussion

An update event is raised after a start event, and the the animation time remains within the an action’s event interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionhandlerprotocol/actionupdated(event:))*