# IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_:_:_:)

**Framework**: IOBluetooth  
**Kind**: func

Allows a client to register for a channel close notification.

**Availability**:
- macOS ?+

## Declaration

```swift
func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(_ channel: IOBluetoothL2CAPChannelRef!, _ callback: IOBluetoothUserNotificationCallback!, _ inRefCon: UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!
```

#### Return Value

Returns an IOBluetoothUserNotificationRef representing the outstanding L2CAP channel close notification. To unregister the notification, call IOBluetoothUserNotificationUnregister() with the returned IOBluetoothUserNotificationRef. If an error is encountered creating the notification, NULL is returned. The returned IOBluetoothUserNotificationRef will be valid for as long as the notification is registered. It is not necessary to retain the result. Once the notification is unregistered, it will no longer be valid.

#### Discussion

The given callback will be called when the L2CAP channel is closed.

## Parameters

- `channel`: The target L2CAP channel
- `callback`: Callback to be called when the L2CAP channel is closed.
- `inRefCon`: Client-supplied refCon to be passed to the callback.

## See Also

- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](iobluetoothignorehiddevice(_:).md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](iobluetoothremoveignoredhiddevice(_:).md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](iobluetoothusernotificationunregister(_:).md)
  Unregisters the target notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothl2capchannelregisterforchannelclosenotification(_:_:_:))*