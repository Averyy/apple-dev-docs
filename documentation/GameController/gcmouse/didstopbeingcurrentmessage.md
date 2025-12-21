# GCMouse.DidStopBeingCurrentMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a mouse stops being the most recently used mouse.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DidStopBeingCurrentMessage
```

#### Overview

Use the `.didStopBeingCurrent` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCMouse.self, for: .didStopBeingCurrent) { message in
   let mouse = message.mouse
}
```

## Topics

### Initializers
- [init(mouse: GCMouse)](gcmouse/didstopbeingcurrentmessage/init(mouse:).md)
### Instance Properties
- [var mouse: GCMouse](gcmouse/didstopbeingcurrentmessage/mouse.md)
  The mouse object that was previously the current mouse.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/didstopbeingcurrentmessage)*