# IOBluetoothRemoveIgnoredHIDDevice(_:)

**Framework**: IOBluetooth  
**Kind**: func

The counterpart to the above IOBluetoothIgnoreHIDDevice() API.

**Availability**:
- macOS ?+

## Declaration

```swift
func IOBluetoothRemoveIgnoredHIDDevice(_ device: IOBluetoothDeviceRef!)
```

## Parameters

- `device`: A Bluetooth Device to “un”ignore.

## See Also

- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](iobluetoothignorehiddevice(_:).md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](iobluetoothl2capchannelregisterforchannelclosenotification(_:_:_:).md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](iobluetoothusernotificationunregister(_:).md)
  Unregisters the target notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothremoveignoredhiddevice(_:))*