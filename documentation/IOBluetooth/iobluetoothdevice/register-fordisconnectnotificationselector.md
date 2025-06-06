# register(forDisconnectNotification:selector:)

**Framework**: IOBluetooth  
**Kind**: method

Allows a client to register for device disconnect notification.

**Availability**:
- macOS ?+

## Declaration

```swift
func register(forDisconnectNotification observer: Any!, selector inSelector: Selector!) -> IOBluetoothUserNotification!
```

#### Return Value

Returns an IOBluetoothUserNotification representing the outstanding device disconnect notification. To unregister the notification, call -unregister of the returned IOBluetoothUserNotification object. If an error is encountered creating the notification, nil is returned.

#### Discussion

The given selector will be called on the target observer when the target device’s connection is closed. The selector should contain two arguments. The first is the user notification object. The second is the IOBluetoothDevice that was disconnected.

## Parameters

- `observer`: Target observer object
- `inSelector`: Selector to be sent to the observer when the connection is destroyed


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothdevice/register(fordisconnectnotification:selector:))*