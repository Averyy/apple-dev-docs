# ColorSyncIterateInstalledProfilesWithOptions(_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncIterateInstalledProfilesWithOptions(_ callBack: ColorSyncProfileIterateCallback?, _ seed: UnsafeMutablePointer<UInt32>?, _ userInfo: UnsafeMutableRawPointer?, _ options: CFDictionary?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?)
```

## See Also

- [func ColorSyncProfileInstall(ColorSyncProfile!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileinstall(_:_:_:_:).md)
- [func ColorSyncProfileUninstall(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileuninstall(_:_:).md)
- [var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String](colorsync_profile_install_entitlement.md)
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](kcolorsyncprofilecomputerdomain.md)
- [var kColorSyncProfileUserDomain: Unmanaged<CFString>!](kcolorsyncprofileuserdomain.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:))*