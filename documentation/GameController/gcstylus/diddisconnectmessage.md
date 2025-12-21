# GCStylus.DidDisconnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a stylus accessory disconnects from the device.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct DidDisconnectMessage
```

#### Overview

Use the `.didDisconnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCStylus.self, for: .didDisconnect) { message in
   let stylus = message.stylus
}
```

## Topics

### Initializers
- [init(stylus: GCStylus)](gcstylus/diddisconnectmessage/init(stylus:).md)
### Instance Properties
- [var stylus: GCStylus](gcstylus/diddisconnectmessage/stylus.md)
  The stylus object that disconnected from the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus/diddisconnectmessage)*