# GCController.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a game controller accessory connects to the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DidConnectMessage
```

#### Overview

Use the `.didConnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCController.self, for: .didConnect) { message in
   let controller = message.controller
}
```

Connections of controller accessories will be reflected in the `controllers` array of the `GCController` class when the message posts.

## Topics

### Initializers
- [init(controller: GCController)](gccontroller/didconnectmessage/init(controller:).md)
### Instance Properties
- [var controller: GCController](gccontroller/didconnectmessage/controller.md)
  The controller object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/didconnectmessage)*