# GCSpatialAccessory.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct  
**Role**: Structure

A message that posts after a spatial accessory connects to the device.

**Availability**:
- visionOS 27.0+

## Declaration

```swift
struct DidConnectMessage
```

#### Overview

Use the `.didConnect` identifier with `NotificationCenter` to listen for this message.

```
let observation = NotificationCenter.default.addObserver(of: GCSpatialAccessory.self, for: .didConnect) { message in
   let accessory = message.spatialAccessory
}
```

Connections of spatial accessories will be reflected in the `spatialAccessories` array of the `GCSpatialAccessory` class when the message posts.

## Topics

### Initializers
- [init(spatialAccessory: GCSpatialAccessory)](./didconnectmessage/init%28spatialaccessory%29.md)
### Instance Properties
- [var spatialAccessory: GCSpatialAccessory](./didconnectmessage/spatialaccessory.md)
  The spatial accessory object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../../Foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcspatialaccessory/didconnectmessage)*