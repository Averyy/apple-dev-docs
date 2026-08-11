# ColorSyncDeviceProfileIterateCallback

**Framework**: ColorSync  
**Kind**: typealias

A callback that ColorSync invokes for each device profile during iteration.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
typealias ColorSyncDeviceProfileIterateCallback = (CFDictionary?, UnsafeMutableRawPointer?) -> Bool
```

#### Discussion

The `colorSyncDeviceProfileInfo` dictionary contains the following keys:

```None
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

- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](colorsyncdevicecopydeviceinfo(_:_:).md)
  Copies information about a device, resolved for the current host and current user.
- [func ColorSyncDeviceSetCustomProfiles(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncdevicesetcustomprofiles(_:_:_:).md)
  Sets custom profiles for a device in lieu of its factory profiles.
- [func ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback!, UnsafeMutableRawPointer?)](colorsynciteratedeviceprofiles(_:_:).md)
  Iterates over the profiles registered for all devices, invoking a callback for each.
- [func ColorSyncProfileCreateDeviceProfile(CFString!, CFUUID!, CFTypeRef!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatedeviceprofile(_:_:_:).md)
  Creates a profile for a device registered with ColorSync.
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncregisterdevice(_:_:_:).md)
  Registers a device of the given class with ColorSync.
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](colorsyncunregisterdevice(_:_:).md)
  Unregisters a device of the given class and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncdeviceprofileiteratecallback)*