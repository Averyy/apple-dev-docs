# GCController.DidStopBeingCurrentMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a game controller stops being the most recently used controller.

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
let observation = NotificationCenter.default.addObserver(of: GCController.self, for: .didStopBeingCurrent) { message in
   let controller = message.controller
}
```

## Topics

### Initializers
- [init(controller: GCController)](gccontroller/didstopbeingcurrentmessage/init(controller:).md)
### Instance Properties
- [var controller: GCController](gccontroller/didstopbeingcurrentmessage/controller.md)
  The controller object that was previously the current controller.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/didstopbeingcurrentmessage)*