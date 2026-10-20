# register(forChannelOpenNotifications:selector:withPSM:direction:)

**Framework**: IOBluetooth  
**Kind**: method

Allows a client to register for L2CAP channel open notifications for certain types of L2CAP channels.

**Availability**:
- macOS ?+

## Declaration

```swift
class func register(forChannelOpenNotifications object: Any!, selector: Selector!, withPSM psm: BluetoothL2CAPPSM, direction inDirection: IOBluetoothUserNotificationChannelDirection) -> IOBluetoothUserNotification!
```

#### Return Value

Returns an IOBluetoothUserNotification representing the outstanding L2CAP channel notification. To unregister the notification, call -unregister on the resulting IOBluetoothUserNotification object. If an error is encountered creating the notification, nil is returned. The returned IOBluetoothUserNotification will be valid for as long as the notification is registered. It is not necessary to retain the result. Once -unregister is called on it, it will no longer be valid.

#### Discussion

The given selector will be called on the target object whenever an L2CAP channel with the given attributes is opened. The selector should accept two arguments. The first is the user notification object. The second is the IOBluetoothL2CAPChannel that was opened.

## Parameters

- `object`: Target object
- `selector`: Selector to be called on the target object when a new L2CAP channel is opened.
- `psm`: PSM to match a new L2CAP channel. If the PSM doesn’t matter, 0 may be passed in.
- `inDirection`: The desired direction of the L2CAP channel - kIOBluetoothUserNotificationChannelDirectionAny if the direction doesn’t matter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/register(forchannelopennotifications:selector:withpsm:direction:))*