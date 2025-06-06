# IOBluetoothIgnoreHIDDevice(_:)

**Framework**: IOBluetooth  
**Kind**: func

Hints that the macOS Bluetooth software should ignore a HID device that connects up.

**Availability**:
- macOS ?+

## Declaration

```swift
func IOBluetoothIgnoreHIDDevice(_ device: IOBluetoothDeviceRef!)
```

## Parameters

- `device`: A Bluetooth Device to ignore.

## See Also

- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](iobluetoothl2capchannelregisterforchannelclosenotification(_:_:_:).md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](iobluetoothremoveignoredhiddevice(_:).md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](iobluetoothusernotificationunregister(_:).md)
  Unregisters the target notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothignorehiddevice(_:))*