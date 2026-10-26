# GCStylusDidDisconnectNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts after a stylus accessory disconnects from the device.

**Availability**:
- visionOS 26.0+

## Declaration

```c
extern NSString * const GCStylusDidDisconnectNotification;
```

## Mentions

- [Discovering and tracking spatial game controllers and styli](./discovering-and-tracking-spatial-game-controllers-and-styli.md)

#### Discussion

Use this constant with `NSNotificationCenter` to listen for stylus disconnection events.

The `object` property of the notification will contain the `GCStylus` that was disconnected.

## See Also

### Accessing the styli
- [class var styli: [GCStylus]](./gcstylus/styli.md)
  Get the collection of stylus accessories currently connected to the device.
- [GCStylusDidConnectNotification](./gcstylusdidconnectnotification.md)
  A notification that posts after a stylus accessory connects to the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylusdiddisconnectnotification)*