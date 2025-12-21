# GCMouse.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a mouse accessory disconnects from the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DidDisconnectMessage
```

#### Overview

Use the `didDisconnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCMouse.self, for: .didDisconnect) { message in
   let mouse = message.mouse
}
```

## Topics

### Initializers
- [init(mouse: GCMouse)](gcmouse/diddisconnectmessage/init(mouse:).md)
### Instance Properties
- [var mouse: GCMouse](gcmouse/diddisconnectmessage/mouse.md)
  The mouse object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/diddisconnectmessage)*