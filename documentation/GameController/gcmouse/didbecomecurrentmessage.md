# GCMouse.DidBecomeCurrentMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a mouse becomes the most recently used mouse.

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

Use the `.didBecomeCurrent` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCMouse.self, for: .didBecomeCurrent) { message in
   let mouse = message.mouse
}
```

## Topics

### Initializers
- [init(mouse: GCMouse)](gcmouse/didbecomecurrentmessage/init(mouse:).md)
### Instance Properties
- [var mouse: GCMouse](gcmouse/didbecomecurrentmessage/mouse.md)
  The mouse object that became current.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/didbecomecurrentmessage)*