# GCRacingWheel.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

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

```
let observation = NotificationCenter.default.addObserver(of: GCRacingWheel.self, for: .didConnect) { message in
   let racingWheel = message.racingWheel
}
```

Connections of controller accessories will be reflected in the `controllers` array of the `GCController` class when the message posts.

## Topics

### Initializers
- [init(racingWheel: GCRacingWheel)](./didconnectmessage/init%28racingwheel%29.md)
### Instance Properties
- [var racingWheel: GCRacingWheel](./didconnectmessage/racingwheel.md)
  The racing wheel object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/didconnectmessage)*