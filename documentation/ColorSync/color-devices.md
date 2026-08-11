# Color devices

**Framework**: ColorSync

Manage the color profiles assigned to displays, printers, scanners, and cameras.

#### Overview

ColorSync tracks the color devices attached to the system and the profiles assigned to each. Register a device, enumerate its profiles, and read or set the factory and custom profiles that describe how it reproduces color. Displays are a color device too: you can find a display’s profile from its display ID and read its gamma and transfer tables. Device profiles are themselves [`ColorSyncProfile`](colorsyncprofile.md) objects. See [`Color profiles`](color-profiles.md).

## Topics

### Registering and enumerating devices
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
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncregisterdevice(_:_:_:).md)
  Registers a device of the given class with ColorSync.
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](colorsyncunregisterdevice(_:_:).md)
  Unregisters a device of the given class and identifier.
### Identifying device classes
- [var kColorSyncCameraDeviceClass: Unmanaged<CFString>!](kcolorsynccameradeviceclass.md)
  The device class for a camera device.
- [var kColorSyncDeviceClass: Unmanaged<CFString>!](kcolorsyncdeviceclass.md)
  A key whose value is one of the device-class constants below.
- [var kColorSyncDisplayDeviceClass: Unmanaged<CFString>!](kcolorsyncdisplaydeviceclass.md)
  The device class for a display device.
- [var kColorSyncPrinterDeviceClass: Unmanaged<CFString>!](kcolorsyncprinterdeviceclass.md)
  The device class for a printer device.
- [var kColorSyncScannerDeviceClass: Unmanaged<CFString>!](kcolorsyncscannerdeviceclass.md)
  The device class for a scanner device.
### Describing devices
- [var kColorSyncDeviceID: Unmanaged<CFString>!](kcolorsyncdeviceid.md)
  A key whose value is the `CFUUIDRef` identifying the device.
- [var kColorSyncDeviceDescription: Unmanaged<CFString>!](kcolorsyncdevicedescription.md)
  A key whose value is the device’s localized name in the current locale.
- [var kColorSyncDeviceDescriptions: Unmanaged<CFString>!](kcolorsyncdevicedescriptions.md)
  A key whose value is a `CFDictionary` of the device’s localized names.
- [var kColorSyncDeviceModeDescription: Unmanaged<CFString>!](kcolorsyncdevicemodedescription.md)
  A key whose value is the device mode’s localized name in the current locale.
- [var kColorSyncDeviceModeDescriptions: Unmanaged<CFString>!](kcolorsyncdevicemodedescriptions.md)
  A key whose value is a `CFDictionary` of the device mode’s localized names.
- [var kColorSyncDeviceHostScope: Unmanaged<CFString>!](kcolorsyncdevicehostscope.md)
  A key specifying the host preference scope of a device; currently only `kCFPreferencesCurrentHost` is supported.
- [var kColorSyncDeviceUserScope: Unmanaged<CFString>!](kcolorsyncdeviceuserscope.md)
  A key specifying the user preference scope of a device; one of `kCFPreferencesCurrentUser` or `kCFPreferencesAnyUser`.
### Describing device profiles
- [var kColorSyncDeviceDefaultProfileID: Unmanaged<CFString>!](kcolorsyncdevicedefaultprofileid.md)
  A key whose value is the ProfileID of the device’s default profile.
- [var kColorSyncDeviceProfileID: Unmanaged<CFString>!](kcolorsyncdeviceprofileid.md)
  A key in the device-profile-info dictionary whose value is the profile’s ProfileID.
- [var kColorSyncDeviceProfileURL: Unmanaged<CFString>!](kcolorsyncdeviceprofileurl.md)
  A key whose value is the `CFURLRef` of a device profile.
- [var kColorSyncDeviceProfileIsCurrent: Unmanaged<CFString>!](kcolorsyncdeviceprofileiscurrent.md)
  A key in the device-profile-info dictionary whose value indicates whether the profile is the current profile.
- [var kColorSyncDeviceProfileIsDefault: Unmanaged<CFString>!](kcolorsyncdeviceprofileisdefault.md)
  A key in the device-profile-info dictionary whose value indicates whether the profile is the default profile.
- [var kColorSyncDeviceProfileIsFactory: Unmanaged<CFString>!](kcolorsyncdeviceprofileisfactory.md)
  A key in the device-profile-info dictionary whose value indicates whether the profile is a factory profile.
- [var kColorSyncProfileHostScope: Unmanaged<CFString>!](kcolorsyncprofilehostscope.md)
  A key specifying the host preference scope of a profile; currently only `kCFPreferencesCurrentHost` is supported.
- [var kColorSyncProfileUserScope: Unmanaged<CFString>!](kcolorsyncprofileuserscope.md)
  A key specifying the user preference scope of a profile; one of `kCFPreferencesCurrentUser` or `kCFPreferencesAnyUser`.
### Accessing custom and factory profiles
- [var kColorSyncCustomProfiles: Unmanaged<CFString>!](kcolorsynccustomprofiles.md)
  A key whose value is a `CFDictionary` describing the device’s custom profiles.
- [var kColorSyncFactoryProfiles: Unmanaged<CFString>!](kcolorsyncfactoryprofiles.md)
  A key whose value is a `CFDictionary` describing the device’s factory profiles.
- [var kColorSyncDoNotSubstituteProfiles: Unmanaged<CFString>!](kcolorsyncdonotsubstituteprofiles.md)
  An option that, when set to `kCFBooleanTrue`, skips substituting a matching system-provided profile.
### Observing device notifications
- [var kColorSyncDeviceProfilesNotification: Unmanaged<CFString>!](kcolorsyncdeviceprofilesnotification.md)
  A notification that ColorSync posts when a device’s profiles change.
- [var kColorSyncDeviceRegisteredNotification: Unmanaged<CFString>!](kcolorsyncdeviceregisterednotification.md)
  A notification that ColorSync posts when a device is registered.
- [var kColorSyncDeviceUnregisteredNotification: Unmanaged<CFString>!](kcolorsyncdeviceunregisterednotification.md)
  A notification that ColorSync posts when a device is unregistered.
- [var kColorSyncDisplayDeviceProfilesNotification: Unmanaged<CFString>!](kcolorsyncdisplaydeviceprofilesnotification.md)
  A notification that ColorSync posts when a display device’s profiles change.
- [var kColorSyncRegistrationUpdateWindowServer: Unmanaged<CFString>!](kcolorsyncregistrationupdatewindowserver.md)
  A notification concerning the window server’s device registration.
### Reading display gamma and profiles
- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithdisplayid(_:).md)
  Creates a profile for the specified display.
- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategammawithdisplayid(_:_:).md)
  Estimates the gamma of the profile for the specified display.
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:).md)
  Converts the profile’s `vcgt` tag to formula components used by `CGSetDisplayTransferByFormula`.
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](colorsyncprofilecreatedisplaytransfertablesfromvcgt(_:_:).md)
  Creates display transfer tables from the profile’s `vcgt` tag.
### Converting display identifiers
- [func CGDisplayCreateUUIDFromDisplayID(UInt32) -> Unmanaged<CFUUID>!](cgdisplaycreateuuidfromdisplayid(_:).md)
- [func CGDisplayGetDisplayIDFromUUID(CFUUID!) -> UInt32](cgdisplaygetdisplayidfromuuid(_:).md)

## See Also

- [Color management modules](color-management-modules.md)
  Work with the Color Management Modules that perform color conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-devices)*