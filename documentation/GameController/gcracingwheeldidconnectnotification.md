# GCRacingWheelDidConnectNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

A notification that posts after a racing wheel controller connects to the device.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```c
extern NSString * const GCRacingWheelDidConnectNotification;
```

## Discussion

The notification object is the [`GCRacingWheel`](./gcracingwheel.md) object that connects to the device.

The system posts this notification on the main thread.

## See Also

### Discovering racing wheels
- [class var connectedRacingWheels: Set<GCRacingWheel>](./gcracingwheel/connectedracingwheels.md)
  The racing wheels connected to the device.
- [GCRacingWheelDidDisconnectNotification](./gcracingwheeldiddisconnectnotification.md)
  A notification that posts after a racing wheel controller disconnects from the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcracingwheeldidconnectnotification)*