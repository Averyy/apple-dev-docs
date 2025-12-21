# GCController.DidBecomeCurrentMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a game controller becomes the most recently used controller.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DidBecomeCurrentMessage
```

#### Overview

This is a good time to swap out UI to match the new current controller, and unregister any handlers with the old current controller.

Use the `.didBecomeCurrent` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCController.self, for: .didBecomeCurrent) { message in
   let controller = message.controller
}
```

## Topics

### Initializers
- [init(controller: GCController)](gccontroller/didbecomecurrentmessage/init(controller:).md)
### Instance Properties
- [var controller: GCController](gccontroller/didbecomecurrentmessage/controller.md)
  The controller object that became current.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/didbecomecurrentmessage)*