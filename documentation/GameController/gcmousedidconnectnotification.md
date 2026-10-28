# GCMouseDidConnectNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts after a mouse connects to the device.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const GCMouseDidConnectNotification;
```

## Discussion

The notification object is a [`GCMouse`](./gcmouse.md) object that represents the mouse.

The system posts this notification on the main thread.

## See Also

### Discovering mouse devices
- [class func mice() -> [GCMouse]](./gcmouse/mice%28%29.md)
  Returns any mice that the user connects to the device.
- [GCMouseDidDisconnectNotification](./gcmousediddisconnectnotification.md)
  A notification that posts after a mouse disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmousedidconnectnotification)*