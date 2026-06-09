# GCSpatialAccessory.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a spatial accessory connects to the device.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DidConnectMessage
```

#### Overview

Use the `.didConnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCSpatialAccessory.self, for: .didConnect) { message in
   let accessory = message.spatialAccessory
}
```

Connections of spatial accessories will be reflected in the `spatialAccessories` array of the `GCSpatialAccessory` class when the message posts.

## Topics

### Initializers
- [init(spatialAccessory: GCSpatialAccessory)](gcspatialaccessory/didconnectmessage/init(spatialaccessory:).md)
### Instance Properties
- [var spatialAccessory: GCSpatialAccessory](gcspatialaccessory/didconnectmessage/spatialaccessory.md)
  The spatial accessory object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcspatialaccessory/didconnectmessage)*