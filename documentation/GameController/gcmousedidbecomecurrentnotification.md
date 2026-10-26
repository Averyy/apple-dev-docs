# GCMouseDidBecomeCurrentNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts when a mouse becomes the most recent mouse that the user connects.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const GCMouseDidBecomeCurrentNotification;
```

#### Discussion

The notification object is a [`GCMouse`](./gcmouse.md) object that represents the current mouse. For example, set the mouse input change handlers when you receive this notification.

The system posts this notification on the main thread.

## See Also

### Handling multiple mouse devices
- [class var current: GCMouse?](./gcmouse/current.md)
  The most recent mouse that the user connects.
- [GCMouseDidStopBeingCurrentNotification](./gcmousedidstopbeingcurrentnotification.md)
  A notification that posts when a mouse stops being the most recent mouse that the user connects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmousedidbecomecurrentnotification)*