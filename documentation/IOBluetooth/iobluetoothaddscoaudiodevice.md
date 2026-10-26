# IOBluetoothAddSCOAudioDevice

**Framework**: IOBluetooth  
**Kind**: func  
**Role**: Function

Creates a persistent audio driver that will route audio data to/from the specified device.

**Availability**:
- macOS 10.0+ - Deprecated in 10.9

## Declaration

```c
extern IOReturn IOBluetoothAddSCOAudioDevice(IOBluetoothDeviceRef device, CFDictionaryRef configDict);
```

#### Return Value

Returns kIOReturnSuccess if the audio driver was successfully created, error if hardware does not support SCO or device is not paired.

#### Discussion

The Bluetooth device must be paired before it can be added. The Bluetooth hardware must also support SCO connections for devices to be added.

When a client attempts to use the audio driver, it will automatically open the baseband connection and the SCO connection if necessary. Once they are open, it will route audio data to/from the audio system. The audio driver will continue to exist (even through reboots) until IOBluetoothRemoveAudioDevice is called.

Currently, the only recognized entry in the configDict is “IOAudioControls”. That entry will be an NSArray of NSDictionary objects where each dictionary represents a single audio control. Following is a description of the mandatory and optional entries in each control dictionary.

Mandatory entries:

kIOAudioControlTypeKey = Four-char-code representing the control type (see IOAudioTypes.h) Possible values: kIOAudioControlTypeLevel kIOAudioControlTypeToggle kIOAudioControlTypeSelector kIOAudioControlSubTypeKey = Four-char-code representing the control subtype. The value is dependent on the control type. Following are common subtypes for each control type: kIOAudioControlTypeLevel: kIOAudioLevelControlSubTypeVolume kIOAudioControlTypeToggle: kIOAudioToggleControlSubTypeMute kIOAudioControlTypeSelector: kIOAudioSelectorControlSubTypeOutput kIOAudioSelectorControlSubTypeInput kIOAudioControlUsageKey = Four-char-code representing the usage of the control (i.e. what part of the I/O chain the control affects - input, output, pass-thru, …) (see IOAudioTypes.h) Possible values: kIOAudioControlUsageOutput kIOAudioControlUsageInput kIOAudioControlUsagePassThru kIOAudioControlChannelIDKey = channel ID for the channel(s) the control acts on (see IOAudioControl.h and IOAudioTypes.h for more info) kIOAudioControlChannelNameKey = name for the channel (see IOAudioControl.h and IOAudioDefines.h for more info) kIOAudioControlValueKey = Initial value of the control - as an NSNumber

Optional entries: kIOAudioControlIDKey = Optional developer-defined ID field used to uniquely identify each control.

Level control-specific entries (see IOAudioDefines.h) kIOAudioLevelControlMinValueKey = Min value for the range for the level control kIOAudioLevelControlMaxValueKey = Max value for the range for the level control kIOAudioLevelControlMinDBKey = Min value in db for the range for the level control. Value is a fixed-point 16.16 number represented as an integer in an NSNumber. kIOAudioLevelControlMaxDBKey = Max value in db for the range for the level control. Value is a fixed-point 16.16 number represented as an integer in an NSNumber.

For a more detailed description of these attributes and how IOAudioControls work, see the headerdoc for IOAudioControl, IOAudioLevelControl, IOAudioToggleControl and IOAudioSelectorControl in the Kernel.framework.

## Parameters

- `device`: A paired Bluetooth audio device
- `configDict`: Configuration dictionary containing a description of the audio controls to be attached to the driver. Passing NULL will result in default controls

## See Also

### Miscellaneous
- [func IOBluetoothIgnoreHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothignorehiddevice%28_%29.md)
  Hints that the macOS Bluetooth software should ignore a HID device that connects up.
- [func IOBluetoothL2CAPChannelRegisterForChannelCloseNotification(IOBluetoothL2CAPChannelRef!, IOBluetoothUserNotificationCallback!, UnsafeMutableRawPointer!) -> Unmanaged<IOBluetoothUserNotificationRef>!](./iobluetoothl2capchannelregisterforchannelclosenotification%28_,_,_%29.md)
  Allows a client to register for a channel close notification.
- [func IOBluetoothRemoveIgnoredHIDDevice(IOBluetoothDeviceRef!)](./iobluetoothremoveignoredhiddevice%28_%29.md)
  The counterpart to the above IOBluetoothIgnoreHIDDevice() API.
- [IOBluetoothRemoveSCOAudioDevice](./iobluetoothremovescoaudiodevice.md)
  Removes a persistent audio driver for a device that had already been added using IOBluetoothAddAudioDevice().
- [func IOBluetoothUserNotificationUnregister(IOBluetoothUserNotificationRef!)](./iobluetoothusernotificationunregister%28_%29.md)
  Unregisters the target notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iobluetooth/iobluetoothaddscoaudiodevice)*