# GCControllerDidBecomeCurrentNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts when a controller becomes the current controller.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```c
extern NSString * const GCControllerDidBecomeCurrentNotification;
```

#### Discussion

The notification object is the [`GCController`](./gccontroller.md) object that’s current.

The system posts this notification on the main thread.

## See Also

### Handling multiple controllers
- [class var current: GCController?](./gccontroller/current.md)
  The most recently used game controller.
- [GCControllerDidStopBeingCurrentNotification](./gccontrollerdidstopbeingcurrentnotification.md)
  A notification that posts when a controller stops being the current controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerdidbecomecurrentnotification)*