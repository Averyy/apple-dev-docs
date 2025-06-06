# ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_:_:_:_:_:_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileGetDisplayTransferFormulaFromVCGT(_ profile: ColorSyncProfile!, _ redMin: UnsafeMutablePointer<Float>!, _ redMax: UnsafeMutablePointer<Float>!, _ redGamma: UnsafeMutablePointer<Float>!, _ greenMin: UnsafeMutablePointer<Float>!, _ greenMax: UnsafeMutablePointer<Float>!, _ greenGamma: UnsafeMutablePointer<Float>!, _ blueMin: UnsafeMutablePointer<Float>!, _ blueMax: UnsafeMutablePointer<Float>!, _ blueGamma: UnsafeMutablePointer<Float>!) -> Bool
```

## See Also

- [func CGDisplayCreateUUIDFromDisplayID(UInt32) -> Unmanaged<CFUUID>!](cgdisplaycreateuuidfromdisplayid(_:).md)
- [func CGDisplayGetDisplayIDFromUUID(CFUUID!) -> UInt32](cgdisplaygetdisplayidfromuuid(_:).md)
- [func ColorSyncCMMCopyCMMIdentifier(ColorSyncCMM!) -> Unmanaged<CFString>?](colorsynccmmcopycmmidentifier(_:).md)
- [func ColorSyncCMMCopyLocalizedName(ColorSyncCMM!) -> Unmanaged<CFString>?](colorsynccmmcopylocalizedname(_:).md)
- [func ColorSyncCMMCreate(CFBundle!) -> Unmanaged<ColorSyncCMM>?](colorsynccmmcreate(_:).md)
- [func ColorSyncCMMGetBundle(ColorSyncCMM!) -> Unmanaged<CFBundle>?](colorsynccmmgetbundle(_:).md)
- [func ColorSyncCMMGetTypeID() -> CFTypeID](colorsynccmmgettypeid().md)
- [func ColorSyncDeviceCopyDeviceInfo(CFString!, CFUUID!) -> Unmanaged<CFDictionary>?](colorsyncdevicecopydeviceinfo(_:_:).md)
- [func ColorSyncDeviceSetCustomProfiles(CFString!, CFUUID!, CFDictionary!) -> Bool](colorsyncdevicesetcustomprofiles(_:_:_:).md)
- [func ColorSyncIterateDeviceProfiles(ColorSyncDeviceProfileIterateCallback!, UnsafeMutableRawPointer?)](colorsynciteratedeviceprofiles(_:_:).md)
- [func ColorSyncIterateInstalledCMMs(ColorSyncCMMIterateCallback!, UnsafeMutableRawPointer?)](colorsynciterateinstalledcmms(_:_:).md)
- [func ColorSyncIterateInstalledProfiles(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofiles(_:_:_:_:).md)
- [func ColorSyncProfileContainsTag(ColorSyncProfile!, CFString!) -> Bool](colorsyncprofilecontainstag(_:_:).md)
- [func ColorSyncProfileCopyData(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<CFData>!](colorsyncprofilecopydata(_:_:).md)
- [func ColorSyncProfileCopyDescriptionString(ColorSyncProfile!) -> Unmanaged<CFString>?](colorsyncprofilecopydescriptionstring(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilegetdisplaytransferformulafromvcgt(_:_:_:_:_:_:_:_:_:_:))*