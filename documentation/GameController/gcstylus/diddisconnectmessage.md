# GCStylus.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a stylus accessory disconnects from the device.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct DidDisconnectMessage
```

## Overview

Use the `.didDisconnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCStylus.self, for: .didDisconnect) { message in
   let stylus = message.stylus
}
```

## Topics

### Initializers
- [init(stylus: GCStylus)](./diddisconnectmessage/init%28stylus%29.md)
### Instance Properties
- [var stylus: GCStylus](./diddisconnectmessage/stylus.md)
  The stylus object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus/diddisconnectmessage)*