# ColorSyncRegisterDevice(_:_:_:)

**Framework**: ColorSync  
**Kind**: func

Registers a device of the given class with ColorSync.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncRegisterDevice(_ deviceClass: CFString!, _ deviceID: CFUUID!, _ deviceInfo: CFDictionary!) -> Bool
```

#### Return Value

`true` on success and `false` in case of failure.

#### Discussion

The `deviceInfo` dictionary requires the following keys:

- [`kColorSyncDeviceDescriptions`](kcolorsyncdevicedescriptions.md): A `CFDictionary` with localized names of the device. Localization keys must be five-character strings containing a language code and region code in the `lc_RG` format, and must contain (at least) the `en_US` locale.
- [`kColorSyncFactoryProfiles`](kcolorsyncfactoryprofiles.md): A `CFDictionary` of factory profile info dictionaries. The keys are the profile IDs and the values are the profile info dictionaries.

It may also include the following optional keys:

- [`kColorSyncDeviceHostScope`](kcolorsyncdevicehostscope.md): The host scope of the device; one of `kCFPreferencesCurrentHost` or `kCFPreferencesAnyHost`. If you don’t specify it, the framework assumes `kCFPreferencesCurrentHost`.
- [`kColorSyncDeviceUserScope`](kcolorsyncdeviceuserscope.md): The user scope of the device; one of `kCFPreferencesCurrentUser` or `kCFPreferencesAnyUser`. If you don’t specify it, the framework assumes `kCFPreferencesCurrentUser`.

The factory profiles dictionary (the value for the key [`kColorSyncFactoryProfiles`](kcolorsyncfactoryprofiles.md) in `deviceInfo`) requires the following keys and values. A ProfileID (of `CFStringRef` type) identifies each profile and serves as the key. The value associated with the key is a profile info dictionary that describes an individual device profile.

- [`kColorSyncDeviceDefaultProfileID`](kcolorsyncdevicedefaultprofileid.md): The associated value must be one of the ProfileIDs present in the dictionary. Presence of this key is not required if there is only one factory profile.

Each profile info `CFDictionary` requires the following keys:

- [`kColorSyncDeviceProfileURL`](kcolorsyncdeviceprofileurl.md): The `CFURLRef` of the profile to register.
- [`kColorSyncDeviceModeDescriptions`](kcolorsyncdevicemodedescriptions.md): A `CFDictionary` with localized device mode names for the profile. Localization keys must be five-character strings containing a language code and region code in the `lc_RG` format, and must contain (at least) the `en_US` locale. For example, `en_US` “Glossy Paper with best quality”.

Example of a `deviceInfo` dictionary:

```None
<<
    kColorSyncDeviceDescriptions   <<
                                        en_US  My Little Printer
                                        de_DE  Mein Kleiner Drucker
                                        fr_FR  Mon petit immprimeur
                                        ...
                                    >>
    kColorSyncFactoryProfiles       <<
                                        CFSTR("Profile 1")  <<
                                                                kColorSyncDeviceProfileURL    {CFURLRef}

                                                                kColorSyncDeviceModeDescriptions    <<
                                                                                                        en_US Glossy Paper
                                                                                                        de_DE Glanzpapier
                                                                                                        fr_FR Papier glace
                                                                                                        ...
                                                                                                    >>
                                        ...

                                        kColorSyncDeviceDefaultProfileID  CFSTR("Profile 1")
                                    >>
    kColorSyncDeviceUserScope   kCFPreferencesAnyUser

    kColorSyncDeviceHostScope   kCFPreferencesCurrentHost
<<
```

> **Note**: Scope for factory profiles is exactly the same as the device scope.

> **Note**: Pass `kCFNull` in lieu of the profile URL, or no URL key/value pair at all, if a factory profile is not available. This enables setting a custom profile.

> **Note**: For compatibility with the legacy API, create the profile keys as `CFString`s from `uint32_t` numbers as follows: `CFStringRef key = CFStringCreateWithFormat(NULL, NULL, CFSTR("%u"), (uint32_t) i);`

## Parameters

- `deviceClass`: The class of the device to register.
- `deviceID`: The identifier of the device to register.
- `deviceInfo`: A dictionary containing the information needed to register a device.

## See Also

- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](colorsyncdevicecopydeviceinfo(_:_:).md)
  Copies information about a device, resolved for the current host and current user.
- [typealias ColorSyncDeviceProfileIterateCallback](colorsyncdeviceprofileiteratecallback.md)
  A callback that ColorSync invokes for each device profile during iteration.
- [func ColorSyncDeviceSetCustomProfiles(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncdevicesetcustomprofiles(_:_:_:).md)
  Sets custom profiles for a device in lieu of its factory profiles.
- [func ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback!, UnsafeMutableRawPointer?)](colorsynciteratedeviceprofiles(_:_:).md)
  Iterates over the profiles registered for all devices, invoking a callback for each.
- [func ColorSyncProfileCreateDeviceProfile(CFString!, CFUUID!, CFTypeRef!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatedeviceprofile(_:_:_:).md)
  Creates a profile for a device registered with ColorSync.
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](colorsyncunregisterdevice(_:_:).md)
  Unregisters a device of the given class and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncregisterdevice(_:_:_:))*