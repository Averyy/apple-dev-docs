# kColorSyncDeviceModeDescriptions

**Framework**: ColorSync  
**Kind**: var

A key whose value is a `CFDictionary` of the device mode’s localized names.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncDeviceModeDescriptions: Unmanaged<CFString>!
```

## See Also

- [var kColorSyncDeviceID: Unmanaged<CFString>!](kcolorsyncdeviceid.md)
  A key whose value is the `CFUUIDRef` identifying the device.
- [var kColorSyncDeviceDescription: Unmanaged<CFString>!](kcolorsyncdevicedescription.md)
  A key whose value is the device’s localized name in the current locale.
- [var kColorSyncDeviceDescriptions: Unmanaged<CFString>!](kcolorsyncdevicedescriptions.md)
  A key whose value is a `CFDictionary` of the device’s localized names.
- [var kColorSyncDeviceModeDescription: Unmanaged<CFString>!](kcolorsyncdevicemodedescription.md)
  A key whose value is the device mode’s localized name in the current locale.
- [var kColorSyncDeviceHostScope: Unmanaged<CFString>!](kcolorsyncdevicehostscope.md)
  A key specifying the host preference scope of a device; currently only `kCFPreferencesCurrentHost` is supported.
- [var kColorSyncDeviceUserScope: Unmanaged<CFString>!](kcolorsyncdeviceuserscope.md)
  A key specifying the user preference scope of a device; one of `kCFPreferencesCurrentUser` or `kCFPreferencesAnyUser`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncdevicemodedescriptions)*