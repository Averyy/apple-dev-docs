# IOBluetoothUserNotificationCallback

**Framework**: IOBluetooth  
**Kind**: typealias

Callback function definition for user notifications.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias IOBluetoothUserNotificationCallback = (UnsafeMutableRawPointer?, IOBluetoothUserNotificationRef?, IOBluetoothObjectRef?) -> Void
```

#### Return Value

None.

#### Discussion

This callback will be invoked when the notification for which it was registered is sent.

## Parameters

- `userRefCon`: (Void *) This user defined parameter was provided during the original call to register the notification.
- `inRef`: (IOBluetoothUserNotificationRef) The notification responsible for sending the notification.
- `status`: (IOBluetoothObjectRef) The object that originated the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationcallback)*