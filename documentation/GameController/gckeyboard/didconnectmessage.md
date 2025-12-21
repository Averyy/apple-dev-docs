# GCKeyboard.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a keyboard accessory connects to the device.

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

Use the `didConnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCKeyboard.self, for: .didConnect) { message in
   let keyboard = message.keyboard
}
```

## Topics

### Initializers
- [init(keyboard: GCKeyboard)](gckeyboard/didconnectmessage/init(keyboard:).md)
### Instance Properties
- [var keyboard: GCKeyboard](gckeyboard/didconnectmessage/keyboard.md)
  The keyboard object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboard/didconnectmessage)*