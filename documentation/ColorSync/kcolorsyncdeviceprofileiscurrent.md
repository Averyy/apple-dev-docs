# kColorSyncDeviceProfileIsCurrent

**Framework**: ColorSync  
**Kind**: var

A key in the device-profile-info dictionary whose value indicates whether the profile is the current profile.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncDeviceProfileIsCurrent: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncDeviceDefaultProfileID: Unmanaged<CFString>!](kcolorsyncdevicedefaultprofileid.md)
  A key whose value is the ProfileID of the device’s default profile.
- [var kColorSyncDeviceProfileID: Unmanaged<CFString>!](kcolorsyncdeviceprofileid.md)
  A key in the device-profile-info dictionary whose value is the profile’s ProfileID.
- [var kColorSyncDeviceProfileURL: Unmanaged<CFString>!](kcolorsyncdeviceprofileurl.md)
  A key whose value is the `CFURLRef` of a device profile.
- [var kColorSyncDeviceProfileIsDefault: Unmanaged<CFString>!](kcolorsyncdeviceprofileisdefault.md)
  A key in the device-profile-info dictionary whose value indicates whether the profile is the default profile.
- [var kColorSyncDeviceProfileIsFactory: Unmanaged<CFString>!](kcolorsyncdeviceprofileisfactory.md)
  A key in the device-profile-info dictionary whose value indicates whether the profile is a factory profile.
- [var kColorSyncProfileHostScope: Unmanaged<CFString>!](kcolorsyncprofilehostscope.md)
  A key specifying the host preference scope of a profile; currently only `kCFPreferencesCurrentHost` is supported.
- [var kColorSyncProfileUserScope: Unmanaged<CFString>!](kcolorsyncprofileuserscope.md)
  A key specifying the user preference scope of a profile; one of `kCFPreferencesCurrentUser` or `kCFPreferencesAnyUser`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncdeviceprofileiscurrent)*