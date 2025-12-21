# GCRacingWheel.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a racing wheel accessory connects to the device.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct DidConnectMessage
```

#### Overview

Use the `.didConnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCRacingWheel.self, for: .didConnect) { message in
   let racingWheel = message.racingWheel
}
```

Connections of controller accessories will be reflected in the `controllers` array of the `GCController` class when the message posts.

## Topics

### Initializers
- [init(racingWheel: GCRacingWheel)](gcracingwheel/didconnectmessage/init(racingwheel:).md)
### Instance Properties
- [var racingWheel: GCRacingWheel](gcracingwheel/didconnectmessage/racingwheel.md)
  The racing wheel object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/didconnectmessage)*