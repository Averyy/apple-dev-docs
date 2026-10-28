# IOBluetoothUserNotificationUnregister(_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Unregisters the target notification.

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothUserNotificationUnregister(_ notificationRef: IOBluetoothUserNotificationRef!)
```

```c
void IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef notificationRef);
```

## Discussion

This function will unregister the notification. Once the notification has been unregistered, it will no longer call the callback. Additionally, once this function has been called the target IOBluetoothUserNotificationRef is no longer valid.

## Parameters

- `notificationRef`: The target IOBluetoothUserNotificationRef to be unregistered

## See Also

### Miscellaneous
- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothignorehiddevice%28_%29.md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](./iobluetoothl2capchannelregisterforchannelclosenotification%28_,_,_%29.md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothremoveignoredhiddevice%28_%29.md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.
- [IOBluetoothAddSCOAudioDevice](./iobluetoothaddscoaudiodevice.md)
  Creates a persistent audio driver that will route audio data to/from the specified device.
- [IOBluetoothRemoveSCOAudioDevice](./iobluetoothremovescoaudiodevice.md)
  Removes a persistent audio driver for a device that had already been added using IOBluetoothAddAudioDevice().


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothusernotificationunregister(_:))*