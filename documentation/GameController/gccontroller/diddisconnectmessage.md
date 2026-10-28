# GCController.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a game controller accessory disconnects from the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DidDisconnectMessage
```

## Overview

Use the `.didDisconnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCController.self, for: .didDisconnect) { message in
   let controller = message.controller
}
```

## Topics

### Initializers
- [init(controller: GCController)](./diddisconnectmessage/init%28controller%29.md)
### Instance Properties
- [var controller: GCController](./diddisconnectmessage/controller.md)
  The controller object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/diddisconnectmessage)*