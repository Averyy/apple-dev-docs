# GCRacingWheel.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a racing wheel accessory disconnects from the device.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct DidDisconnectMessage
```

## Overview

Use the `.didDisconnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCRacingWheel.self, for: .didDisconnect) { message in
   let racingWheel = message.racingWheel
}
```

## Topics

### Initializers
- [init(racingWheel: GCRacingWheel)](./diddisconnectmessage/init%28racingwheel%29.md)
### Instance Properties
- [var racingWheel: GCRacingWheel](./diddisconnectmessage/racingwheel.md)
  The racing wheel object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheel/diddisconnectmessage)*