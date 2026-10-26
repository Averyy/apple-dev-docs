# GCSpatialAccessoryDidConnectNotification

**Framework**: Game Controller  
**Kind**: var  
**Role**: Global Variable

Use these constants with NSNotificationCenter to listen to connection and disconnection events.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern NSString * const GCSpatialAccessoryDidConnectNotification;
```

#### Discussion

Use GCSpatialAccessoryDidConnectNotification for observing connections of spatial accessories. Use GCSpatialAccessoryDidDisconnectNotification for observing disconnections of spatial accessories.

Connections and disconnections of spatial accessories will also be reflected in the accessories array of the GCSpatialAccessory class.

The ‘object’ property of the notification will contain the GCSpatialAccessory that was connected or disconnected.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcspatialaccessorydidconnectnotification)*