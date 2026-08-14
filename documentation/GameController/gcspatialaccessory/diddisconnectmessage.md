# GCSpatialAccessory.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a spatial accessory disconnects from the device.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DidDisconnectMessage
```

#### Overview

Use the `.didDisconnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCSpatialAccessory.self, for: .didDisconnect) { message in
   let spatialAccessory = message.spatialAccessory
}
```

## Topics

### Initializers
- [init(spatialAccessory: GCSpatialAccessory)](gcspatialaccessory/diddisconnectmessage/init(spatialaccessory:).md)
### Instance Properties
- [var spatialAccessory: GCSpatialAccessory](gcspatialaccessory/diddisconnectmessage/spatialaccessory.md)
  The spatial object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../foundation/notificationcenter/mainactormessage.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcspatialaccessory/diddisconnectmessage)*