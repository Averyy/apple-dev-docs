# Color devices

**Framework**: ColorSync

Manage the color profiles assigned to displays, printers, scanners, and cameras.

#### Overview

ColorSync tracks the color devices attached to the system and the profiles assigned to each. Register a device, enumerate its profiles, and read or set the factory and custom profiles that describe how it reproduces color. Displays are a color device too: you can find a display’s profile from its display ID and read its gamma and transfer tables. Device profiles are themselves [`ColorSyncProfile`](colorsyncprofile.md) objects. See [`Color profiles`](color-profiles.md).

## Topics

### Registering and enumerating devices
- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](colorsyncdevicecopydeviceinfo(_:_:).md)
- [typealias ColorSyncDeviceProfileIterateCallback](colorsyncdeviceprofileiteratecallback.md)
- [func ColorSyncDeviceSetCustomProfiles(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncdevicesetcustomprofiles(_:_:_:).md)
- [func ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback!, UnsafeMutableRawPointer?)](colorsynciteratedeviceprofiles(_:_:).md)
- [func ColorSyncProfileCreateDeviceProfile(CFString!, CFUUID!, CFTypeRef!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatedeviceprofile(_:_:_:).md)
- [func ColorSyncRegisterDevice(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncregisterdevice(_:_:_:).md)
- [func ColorSyncUnregisterDevice(CFString!, CFUUID!) -> Bool](colorsyncunregisterdevice(_:_:).md)
### Identifying device classes
- [var kColorSyncCameraDeviceClass: Unmanaged<CFString>!](kcolorsynccameradeviceclass.md)
- [var kColorSyncDeviceClass: Unmanaged<CFString>!](kcolorsyncdeviceclass.md)
- [var kColorSyncDisplayDeviceClass: Unmanaged<CFString>!](kcolorsyncdisplaydeviceclass.md)
- [var kColorSyncPrinterDeviceClass: Unmanaged<CFString>!](kcolorsyncprinterdeviceclass.md)
- [var kColorSyncScannerDeviceClass: Unmanaged<CFString>!](kcolorsyncscannerdeviceclass.md)
### Describing devices
- [var kColorSyncDeviceID: Unmanaged<CFString>!](kcolorsyncdeviceid.md)
- [var kColorSyncDeviceDescription: Unmanaged<CFString>!](kcolorsyncdevicedescription.md)
- [var kColorSyncDeviceDescriptions: Unmanaged<CFString>!](kcolorsyncdevicedescriptions.md)
- [var kColorSyncDeviceModeDescription: Unmanaged<CFString>!](kcolorsyncdevicemodedescription.md)
- [var kColorSyncDeviceModeDescriptions: Unmanaged<CFString>!](kcolorsyncdevicemodedescriptions.md)
- [var kColorSyncDeviceHostScope: Unmanaged<CFString>!](kcolorsyncdevicehostscope.md)
- [var kColorSyncDeviceUserScope: Unmanaged<CFString>!](kcolorsyncdeviceuserscope.md)
### Describing device profiles
- [var kColorSyncDeviceDefaultProfileID: Unmanaged<CFString>!](kcolorsyncdevicedefaultprofileid.md)
- [var kColorSyncDeviceProfileID: Unmanaged<CFString>!](kcolorsyncdeviceprofileid.md)
- [var kColorSyncDeviceProfileURL: Unmanaged<CFString>!](kcolorsyncdeviceprofileurl.md)
- [var kColorSyncDeviceProfileIsCurrent: Unmanaged<CFString>!](kcolorsyncdeviceprofileiscurrent.md)
- [var kColorSyncDeviceProfileIsDefault: Unmanaged<CFString>!](kcolorsyncdeviceprofileisdefault.md)
- [var kColorSyncDeviceProfileIsFactory: Unmanaged<CFString>!](kcolorsyncdeviceprofileisfactory.md)
- [var kColorSyncProfileHostScope: Unmanaged<CFString>!](kcolorsyncprofilehostscope.md)
- [var kColorSyncProfileUserScope: Unmanaged<CFString>!](kcolorsyncprofileuserscope.md)
### Accessing custom and factory profiles
- [var kColorSyncCustomProfiles: Unmanaged<CFString>!](kcolorsynccustomprofiles.md)
- [var kColorSyncFactoryProfiles: Unmanaged<CFString>!](kcolorsyncfactoryprofiles.md)
- [var kColorSyncDoNotSubstituteProfiles: Unmanaged<CFString>!](kcolorsyncdonotsubstituteprofiles.md)
### Observing device notifications
- [var kColorSyncDeviceProfilesNotification: Unmanaged<CFString>!](kcolorsyncdeviceprofilesnotification.md)
- [var kColorSyncDeviceRegisteredNotification: Unmanaged<CFString>!](kcolorsyncdeviceregisterednotification.md)
- [var kColorSyncDeviceUnregisteredNotification: Unmanaged<CFString>!](kcolorsyncdeviceunregisterednotification.md)
- [var kColorSyncDisplayDeviceProfilesNotification: Unmanaged<CFString>!](kcolorsyncdisplaydeviceprofilesnotification.md)
- [var kColorSyncRegistrationUpdateWindowServer: Unmanaged<CFString>!](kcolorsyncregistrationupdatewindowserver.md)
### Reading display gamma and profiles
- [func ColorSyncProfileCreateWithDisplayID(UInt32) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithdisplayid(_:).md)
- [func ColorSyncProfileEstimateGammaWithDisplayID(Int32, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Float](colorsyncprofileestimategammawithdisplayid(_:_:).md)
- [func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!, UnsafeMutablePointer<Float>!) -> Bool](colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:).md)
- [func ColorSyncProfileCreateDisplayTransferTablesFromVCGT(ColorSyncProfile!, UnsafeMutablePointer<Int>!) -> Unmanaged<CFData>?](colorsyncprofilecreatedisplaytransfertablesfromvcgt(_:_:).md)
### Converting display identifiers
- [func CGDisplayCreateUUIDFromDisplayID(UInt32) -> Unmanaged<CFUUID>!](cgdisplaycreateuuidfromdisplayid(_:).md)
- [func CGDisplayGetDisplayIDFromUUID(CFUUID!) -> UInt32](cgdisplaygetdisplayidfromuuid(_:).md)

## See Also

- [Color management modules](color-management-modules.md)
  Work with the Color Management Modules that perform color conversions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/color-devices)*