# IOBluetoothRemoveIgnoredHIDDevice(_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

The counterpart to the above IOBluetoothIgnoreHIDDevice() API.

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothRemoveIgnoredHIDDevice(_ device: IOBluetoothDeviceRef!)
```

```c
extern void IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef device);
```

## Parameters

- `device`: A Bluetooth Device to “un”ignore.

## See Also

### Miscellaneous
- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothignorehiddevice%28_%29.md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](./iobluetoothl2capchannelregisterforchannelclosenotification%28_,_,_%29.md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](./iobluetoothusernotificationunregister%28_%29.md)
  Unregisters the target notification.
- [IOBluetoothAddSCOAudioDevice](./iobluetoothaddscoaudiodevice.md)
  Creates a persistent audio driver that will route audio data to/from the specified device.
- [IOBluetoothRemoveSCOAudioDevice](./iobluetoothremovescoaudiodevice.md)
  Removes a persistent audio driver for a device that had already been added using IOBluetoothAddAudioDevice().


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothremoveignoredhiddevice(_:))*