# GCKeyboard.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a keyboard accessory disconnects from the device.

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

#### Overview

Use the `didDisconnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCKeyboard.self, for: .didDisconnect) { message in
   let keyboard = message.keyboard
}
```

## Topics

### Initializers
- [init(keyboard: GCKeyboard)](./diddisconnectmessage/init%28keyboard%29.md)
### Instance Properties
- [var keyboard: GCKeyboard](./diddisconnectmessage/keyboard.md)
  The keyboard object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboard/diddisconnectmessage)*