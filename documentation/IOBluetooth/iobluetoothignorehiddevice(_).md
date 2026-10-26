# IOBluetoothIgnoreHIDDevice(_:)

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Hints that the macOS Bluetooth software should ignore a HID device that connects up.

**Availability**:
- macOS

## Declaration

```swift
func IOBluetoothIgnoreHIDDevice(_ device: IOBluetoothDeviceRef!)
```

```c
extern void IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef device);
```

## Parameters

- `device`: A Bluetooth Device to ignore.

## See Also

### Miscellaneous
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](./iobluetoothl2capchannelregisterforchannelclosenotification%28_,_,_%29.md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothremoveignoredhiddevice%28_%29.md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](./iobluetoothusernotificationunregister%28_%29.md)
  Unregisters the target notification.
- [IOBluetoothAddSCOAudioDevice](./iobluetoothaddscoaudiodevice.md)
  Creates a persistent audio driver that will route audio data to/from the specified device.
- [IOBluetoothRemoveSCOAudioDevice](./iobluetoothremovescoaudiodevice.md)
  Removes a persistent audio driver for a device that had already been added using IOBluetoothAddAudioDevice().


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothignorehiddevice(_:))*