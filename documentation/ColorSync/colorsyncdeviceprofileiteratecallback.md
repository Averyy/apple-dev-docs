# ColorSyncDeviceProfileIterateCallback

**Framework**: ColorSync  
**Kind**: typealias  
**Role**: Type Alias

A callback that ColorSync invokes for each device profile during iteration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
typealias ColorSyncDeviceProfileIterateCallback = (CFDictionary?, UnsafeMutableRawPointer?) -> Bool
```

```c
typedef _Bool (*)(const struct __CFDictionary *, void *) ColorSyncDeviceProfileIterateCallback;
```

## Discussion

The `colorSyncDeviceProfileInfo` dictionary contains the following keys:

```
kColorSyncDeviceClass              {camera, display, printer, scanner}
kColorSyncDeviceID                 {CFUUIDRef registered with ColorSync}
kColorSyncDeviceDescription        {localized device description}
kColorSyncDeviceModeDescription    {localized device mode description}
kColorSyncDeviceProfileID          {ProfileID registered with ColorSync}
kColorSyncDeviceProfileURL         {CFURLRef registered with ColorSync}
kColorSyncDeviceProfileIsFactory   {kCFBooleanTrue or kCFBooleanFalse}
kColorSyncDeviceProfileIsDefault   {kCFBooleanTrue or kCFBooleanFalse}
kColorSyncDeviceProfileIsCurrent   {kCFBooleanTrue or kCFBooleanFalse}
```

## Parameters

- `colorSyncDeviceProfileInfo`: A dictionary describing the device profile.
- `userInfo`: The user info passed to the iteration function. Optional.

## See Also

### Registering and enumerating devices
- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](./colorsyncdevicecopydeviceinfo%28_,_%29.md)
  Copies information about a device, resolved for the current host and current user.
- [func ColorSyncDeviceSetCustomProfiles(CFString!, CFUUID!, CFDictionary!) -> Bool](./colorsyncdevicesetcustomprofiles%28_,_,_%29.md)
  Sets custom profiles for a device in lieu of its factory profiles.
- [func ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback!, UnsafeMutableRawPointer?)](./colorsynciteratedeviceprofiles%28_,_%29.md)
  Iterates over the profiles registered for all devices, invoking a callback for each.
- [func ColorSyncProfileCreateDeviceProfile(CFString!, CFUUID!, CFTypeRef!) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatedeviceprofile%28_,_,_%29.md)
  Creates a profile for a device registered with ColorSync.
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](./colorsyncregisterdevice%28_,_,_%29.md)
  Registers a device of the given class with ColorSync.
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](./colorsyncunregisterdevice%28_,_%29.md)
  Unregisters a device of the given class and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncdeviceprofileiteratecallback)*