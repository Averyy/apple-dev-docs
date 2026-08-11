# ColorSyncDeviceSetCustomProfiles(_:_:_:)

**Framework**: ColorSync  
**Kind**: func

Sets custom profiles for a device in lieu of its factory profiles.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncDeviceSetCustomProfiles(_ deviceClass: CFString!, _ deviceID: CFUUID!, _ profileInfo: CFDictionary!) -> Bool
```

#### Return Value

`true` on success and `false` in case of failure.

#### Discussion

The `profileInfo` dictionary requires the following keys:

- ProfileIDs, which must be a subset of the ProfileIDs you registered the device with, or [`kColorSyncDeviceDefaultProfileID`](kcolorsyncdevicedefaultprofileid.md) for setting a custom default profile.

It requires the following values:

- The `CFURLRef` of the profile to set as a custom profile.

It may also include the following optional keys:

- [`kColorSyncProfileHostScope`](kcolorsyncprofilehostscope.md): The host scope of the profile; one of `kCFPreferencesCurrentHost` or `kCFPreferencesAnyHost`. If you don’t specify it, the framework assumes `kCFPreferencesCurrentHost`.
- [`kColorSyncProfileUserScope`](kcolorsyncprofileuserscope.md): The user scope of the profile; one of `kCFPreferencesCurrentUser` or `kCFPreferencesAnyUser`. If you don’t specify it, the framework assumes `kCFPreferencesCurrentUser`.

> **Note**: Profile scope for custom profiles cannot exceed the scope of the factory profiles.

> **Note**: There is only one host scope and user scope per dictionary (that is, per call).

> **Note**: Pass `kCFNull` in lieu of the profile URL to unset the custom profile and reset the current profile to the factory profile.

## Parameters

- `deviceClass`: The class of the device.
- `deviceID`: The identifier of the device.
- `profileInfo`: A `CFDictionary` containing the information about custom profiles to set in lieu of factory profiles.

## See Also

- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](colorsyncdevicecopydeviceinfo(_:_:).md)
  Copies information about a device, resolved for the current host and current user.
- [typealias ColorSyncDeviceProfileIterateCallback](colorsyncdeviceprofileiteratecallback.md)
  A callback that ColorSync invokes for each device profile during iteration.
- [func ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback!, UnsafeMutableRawPointer?)](colorsynciteratedeviceprofiles(_:_:).md)
  Iterates over the profiles registered for all devices, invoking a callback for each.
- [func ColorSyncProfileCreateDeviceProfile(CFString!, CFUUID!, CFTypeRef!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatedeviceprofile(_:_:_:).md)
  Creates a profile for a device registered with ColorSync.
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncregisterdevice(_:_:_:).md)
  Registers a device of the given class with ColorSync.
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](colorsyncunregisterdevice(_:_:).md)
  Unregisters a device of the given class and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncdevicesetcustomprofiles(_:_:_:))*