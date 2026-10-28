# GCKeyboard.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a keyboard accessory connects to the device.

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
let observation = NotificationCenter.default.addObserver(of: GCKeyboard.self, for: .didConnect) { message in
   let keyboard = message.keyboard
}
```

## Topics

### Initializers
- [init(keyboard: GCKeyboard)](./didconnectmessage/init%28keyboard%29.md)
### Instance Properties
- [var keyboard: GCKeyboard](./didconnectmessage/keyboard.md)
  The keyboard object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboard/didconnectmessage)*