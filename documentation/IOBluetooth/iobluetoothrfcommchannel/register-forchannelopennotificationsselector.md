# register(forChannelOpenNotifications:selector:)

**Framework**: IOBluetooth  
**Kind**: method

Allows a client to register for RFCOMM channel open notifications for any RFCOMM channel.

**Availability**:
- macOS ?+

## Declaration

```swift
class func register(forChannelOpenNotifications object: Any!, selector: Selector!) -> IOBluetoothUserNotification!
```

#### Return Value

Returns an IOBluetoothUserNotification representing the outstanding RFCOMM channel notification. To unregister the notification, call -unregister on the resulting IOBluetoothUserNotification object. If an error is encountered creating the notification, nil is returned. The returned IOBluetoothUserNotification will be valid for as long as the notification is registered. It is not necessary to retain the result. Once -unregister is called on it, it will no longer be valid.

#### Discussion

The given selector will be called on the target object whenever any RFCOMM channel is opened. The selector should accept two arguments. The first is the user notification object. The second is the IOBluetoothRFCOMMChannel that was opened.

## Parameters

- `object`: Target object
- `selector`: Selector to be called on the target object when a new RFCOMM channel is opened. the format for the selector is: -(void) selectorName:(IOBluetoothUserNotification *)inNotification channel:(IOBluetoothRFCOMMChannel *)newChannel


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothrfcommchannel/register(forchannelopennotifications:selector:))*