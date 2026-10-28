# GCController.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a game controller accessory connects to the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DidConnectMessage
```

## Overview

Use the `.didConnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCController.self, for: .didConnect) { message in
   let controller = message.controller
}
```

Connections of controller accessories will be reflected in the `controllers` array of the `GCController` class when the message posts.

## Topics

### Initializers
- [init(controller: GCController)](./didconnectmessage/init%28controller%29.md)
### Instance Properties
- [var controller: GCController](./didconnectmessage/controller.md)
  The controller object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/didconnectmessage)*