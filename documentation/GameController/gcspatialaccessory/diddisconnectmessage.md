# GCSpatialAccessory.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a spatial accessory disconnects from the device.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
struct DidDisconnectMessage
```

#### Overview

Use the `.didDisconnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCSpatialAccessory.self, for: .didDisconnect) { message in
   let spatialAccessory = message.spatialAccessory
}
```

## Topics

### Initializers
- [init(spatialAccessory: GCSpatialAccessory)](./diddisconnectmessage/init%28spatialaccessory%29.md)
### Instance Properties
- [var spatialAccessory: GCSpatialAccessory](./diddisconnectmessage/spatialaccessory.md)
  The spatial object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcspatialaccessory/diddisconnectmessage)*