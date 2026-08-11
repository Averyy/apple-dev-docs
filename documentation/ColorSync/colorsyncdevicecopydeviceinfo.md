# ColorSyncDeviceCopyDeviceInfo(_:_:)

**Framework**: ColorSync  
**Kind**: func

Copies information about a device, resolved for the current host and current user.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncDeviceCopyDeviceInfo(_ deviceClass: CFString!, _ devID: CFUUID!) -> Unmanaged<CFDictionary>?
```

#### Return Value

A dictionary describing the device, or `NULL` if no matching device is registered.

#### Discussion

Returns a dictionary with the following keys and values resolved for the current host and current user:

```None
<<
    kColorSyncDeviceClass                   {camera, display, printer, scanner}
    kColorSyncDeviceID                      {CFUUIDRef registered with ColorSync}
    kColorSyncDeviceDescription             {localized device description}
    kColorSyncFactoryProfiles  (dictionary) <<
                                                {ProfileID}    (dictionary) <<
                                                                                kColorSyncDeviceProfileURL      {CFURLRef or kCFNull}
                                                                                kColorSyncDeviceModeDescription {localized mode description}
                                                                            >>
                                                 ...
                                                kColorSyncDeviceDefaultProfileID {ProfileID}
                                            >>
    kColorSyncCustomProfiles  (dictionary) <<
                                                {ProfileID}    {CFURLRef or kCFNull}
                                                ...
                                           <<
    kColorSyncDeviceUserScope              {kCFPreferencesAnyUser or kCFPreferencesCurrentUser}
    kColorSyncDeviceHostScope              {kCFPreferencesAnyHost or kCFPreferencesCurrentHost}
>>
```

## Parameters

- `deviceClass`: The class of the device.
- `devID`: The identifier of the device.

## See Also

- [typealias ColorSyncDeviceProfileIterateCallback](colorsyncdeviceprofileiteratecallback.md)
  A callback that ColorSync invokes for each device profile during iteration.
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

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncdevicecopydeviceinfo(_:_:))*