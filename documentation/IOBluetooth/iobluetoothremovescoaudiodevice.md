# IOBluetoothRemoveSCOAudioDevice

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Removes a persistent audio driver for a device that had already been added using IOBluetoothAddAudioDevice().

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

## Declaration

```c
extern IOReturn IOBluetoothRemoveSCOAudioDevice(IOBluetoothDeviceRef device);
```

## Return Value

Returns kIOReturnSuccess if the audio driver was successfully removed.

## Parameters

- `device`: Bluetooth audio device to remove

## See Also

### Miscellaneous
- [IOBluetoothAddSCOAudioDevice](./iobluetoothaddscoaudiodevice.md)
  Creates a persistent audio driver that will route audio data to/from the specified device.
- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothignorehiddevice%28_%29.md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](./iobluetoothl2capchannelregisterforchannelclosenotification%28_,_,_%29.md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothremoveignoredhiddevice%28_%29.md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](./iobluetoothusernotificationunregister%28_%29.md)
  Unregisters the target notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothremovescoaudiodevice)*