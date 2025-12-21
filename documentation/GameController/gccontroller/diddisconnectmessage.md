# GCController.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a game controller accessory disconnects from the device.

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

Use the `.didDisconnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCController.self, for: .didDisconnect) { message in
   let controller = message.controller
}
```

## Topics

### Initializers
- [init(controller: GCController)](gccontroller/diddisconnectmessage/init(controller:).md)
### Instance Properties
- [var controller: GCController](gccontroller/diddisconnectmessage/controller.md)
  The controller object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/diddisconnectmessage)*