# register(forChannelCloseNotification:selector:)

**Framework**: IOBluetooth  
**Kind**: method

Allows a client to register for a channel close notification.

**Availability**:
- macOS ?+

## Declaration

```swift
func register(forChannelCloseNotification observer: Any!, selector inSelector: Selector!) -> IOBluetoothUserNotification!
```

#### Return Value

Returns an IOBluetoothUserNotification representing the outstanding L2CAP channel close notification. To unregister the notification, call -unregister of the returned IOBluetoothUserNotification object. If an error is encountered creating the notification, nil is returned.

#### Discussion

The given selector will be called on the target observer when the L2CAP channel is closed. The selector should contain two arguments. The first is the user notification object. The second is the IOBluetoothL2CAPChannel that was closed.

## Parameters

- `observer`: Target observer object
- `inSelector`: Selector to be sent to the observer when the L2CAP channel is closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannel/register(forchannelclosenotification:selector:))*