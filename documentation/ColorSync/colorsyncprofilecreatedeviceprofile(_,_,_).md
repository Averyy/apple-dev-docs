# ColorSyncProfileCreateDeviceProfile(_:_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Creates a profile for a device registered with ColorSync.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileCreateDeviceProfile(_ deviceClass: CFString!, _ deviceID: CFUUID!, _ profileID: CFTypeRef!) -> Unmanaged<ColorSyncProfile>?
```

```c
extern ColorSyncProfileRefColorSyncProfileCreateDeviceProfile(CFStringRef deviceClass, CFUUIDRef deviceID, CFTypeRef profileID);
```

#### Return Value

A new profile, or `NULL` in case of failure.

#### Discussion

See `ColorSyncDevice.h` for more information on `deviceClass`, `deviceID`, and `profileID`.

## Parameters

- `deviceClass`: The ColorSync device class.
- `deviceID`: The device ID registered with ColorSync.
- `profileID`: The profile ID registered with ColorSync; pass [`kColorSyncDeviceDefaultProfileID`](./kcolorsyncdevicedefaultprofileid.md) to get the default profile.

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
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](./colorsyncregisterdevice%28_,_,_%29.md)
  Registers a device of the given class with ColorSync.
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](./colorsyncunregisterdevice%28_,_%29.md)
  Unregisters a device of the given class and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatedeviceprofile(_:_:_:))*