# IOBluetoothUserNotificationUnregister(_:)

**Framework**: IOBluetooth  
**Kind**: func

Unregisters the target notification.

**Availability**:
- macOS ?+

## Declaration

```swift
func IOBluetoothUserNotificationUnregister(_ notificationRef: IOBluetoothUserNotificationRef!)
```

#### Discussion

This function will unregister the notification. Once the notification has been unregistered, it will no longer call the callback. Additionally, once this function has been called the target IOBluetoothUserNotificationRef is no longer valid.

## Parameters

- `notificationRef`: The target IOBluetoothUserNotificationRef to be unregistered

## See Also

- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](iobluetoothignorehiddevice(_:).md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](iobluetoothl2capchannelregisterforchannelclosenotification(_:_:_:).md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](iobluetoothremoveignoredhiddevice(_:).md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationunregister(_:))*