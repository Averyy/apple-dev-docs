# COLORSYNC_PROFILE_INSTALL_ENTITLEMENT

**Framework**: ColorSync  
**Kind**: var

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String { get }
```

## See Also

- [func ColorSyncProfileInstall(ColorSyncProfile!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileinstall(_:_:_:_:).md)
  Installs a profile in the specified domain.
- [func ColorSyncProfileUninstall(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileuninstall(_:_:).md)
  Uninstalls a profile.
- [func ColorSyncIterateInstalledProfilesWithOptions(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:).md)
  Iterates over the installed profiles, using the given options.
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](kcolorsyncprofilecomputerdomain.md)
  The profile domain for profiles shared by all users of the computer.
- [var kColorSyncProfileUserDomain: Unmanaged<CFString>!](kcolorsyncprofileuserdomain.md)
  The profile domain for the current user’s profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsync_profile_install_entitlement)*