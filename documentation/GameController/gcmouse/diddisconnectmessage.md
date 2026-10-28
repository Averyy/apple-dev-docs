# GCMouse.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a mouse accessory disconnects from the device.

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

Use the `didDisconnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCMouse.self, for: .didDisconnect) { message in
   let mouse = message.mouse
}
```

## Topics

### Initializers
- [init(mouse: GCMouse)](./diddisconnectmessage/init%28mouse%29.md)
### Instance Properties
- [var mouse: GCMouse](./diddisconnectmessage/mouse.md)
  The mouse object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmouse/diddisconnectmessage)*