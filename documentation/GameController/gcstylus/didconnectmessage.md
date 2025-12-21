# GCStylus.DidConnectMessage

**Framework**: Game Controller  
**Kind**: struct

A message that posts after a stylus accessory connects to the device.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
struct DidConnectMessage
```

#### Overview

Use the `.didConnect` identifier with `NotificationCenter` to listen for this message.

```None
let observation = NotificationCenter.default.addObserver(of: GCStylus.self, for: .didCnnect) { message in
   let stylus = message.stylus
}
```

Connections of stylus accessories will be reflected in the `styli` array of the `GCStylus` class when the message posts.

## Topics

### Initializers
- [init(stylus: GCStylus)](gcstylus/didconnectmessage/init(stylus:).md)
### Instance Properties
- [var stylus: GCStylus](gcstylus/didconnectmessage/stylus.md)
  The stylus object that connected to the device.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus/didconnectmessage)*