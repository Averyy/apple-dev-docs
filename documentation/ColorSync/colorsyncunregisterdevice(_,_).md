# ColorSyncUnregisterDevice(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Unregisters a device of the given class and identifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncUnregisterDevice(_ deviceClass: CFString!, _ deviceID: CFUUID!) -> Bool
```

```c
extern bool ColorSyncUnregisterDevice(CFStringRef deviceClass, CFUUIDRef deviceID);
```

#### Return Value

`true` on success and `false` in case of failure.

## Parameters

- `deviceClass`: The class of the device to unregister.
- `deviceID`: The identifier of the device to unregister.

## See Also

### Registering and enumerating devices
- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](./colorsyncdevicecopydeviceinfo%28_,_%29.md)
  Copies information about a device, resolved for the current host and current user.
- [typealias ColorSyncDeviceProfileIterateCallback](./colorsyncdeviceprofileiteratecallback.md)
  A callback that ColorSync invokes for each device profile during iteration.
- [func ColorSyncDeviceSetCustomProfiles(CFString!, CFUUID!, CFDictionary!) -> Bool](./colorsyncdevicesetcustomprofiles%28_,_,_%29.md)
  Sets custom profiles for a device in lieu of its factory profiles.
- [func ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback!, UnsafeMutableRawPointer?)](./colorsynciteratedeviceprofiles%28_,_%29.md)
  Iterates over the profiles registered for all devices, invoking a callback for each.
- [func ColorSyncProfileCreateDeviceProfile(CFString!, CFUUID!, CFTypeRef!) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatedeviceprofile%28_,_,_%29.md)
  Creates a profile for a device registered with ColorSync.
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](./colorsyncregisterdevice%28_,_,_%29.md)
  Registers a device of the given class with ColorSync.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncunregisterdevice(_:_:))*