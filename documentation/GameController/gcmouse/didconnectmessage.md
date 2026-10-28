# GCMouse.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a mouse accessory connects to the device.

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

Use the `didConnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCMouse.self, for: .didConnect) { message in
   let mouse = message.mouse
}
```

Connections of mouse accessories will be reflected in the `mice` array of the `GCMouse` class when the message posts.

## Topics

### Initializers
- [init(mouse: GCMouse)](./didconnectmessage/init%28mouse%29.md)
### Instance Properties
- [var mouse: GCMouse](./didconnectmessage/mouse.md)
  The mouse object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/didconnectmessage)*