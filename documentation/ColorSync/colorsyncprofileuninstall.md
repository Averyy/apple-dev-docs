# ColorSyncProfileUninstall(_:_:)

**Framework**: ColorSync  
**Kind**: func

Uninstalls a profile.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileUninstall(_ profile: ColorSyncProfile!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

#### Return Value

`true` on success, or `false` in case of error.

#### Discussion

The profile must return a valid URL for [`ColorSyncProfileGetURL(_:_:)`](colorsyncprofilegeturl(_:_:).md); that is, it must be created with [`ColorSyncProfileCreateWithURL(_:_:)`](colorsyncprofilecreatewithurl(_:_:).md). Also, the URL must be in either [`kColorSyncProfileComputerDomain`](kcolorsyncprofilecomputerdomain.md) or [`kColorSyncProfileUserDomain`](kcolorsyncprofileuserdomain.md), including subfolders of those.

Using this function requires `COLORSYNC_PROFILE_INSTALL_ENTITLEMENT`.

## Parameters

- `profile`: The profile to uninstall.
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

- [func ColorSyncProfileInstall(ColorSyncProfile!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileinstall(_:_:_:_:).md)
  Installs a profile in the specified domain.
- [func ColorSyncIterateInstalledProfilesWithOptions(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:).md)
  Iterates over the installed profiles, using the given options.
- [var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String](colorsync_profile_install_entitlement.md)
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](kcolorsyncprofilecomputerdomain.md)
  The profile domain for profiles shared by all users of the computer.
- [var kColorSyncProfileUserDomain: Unmanaged<CFString>!](kcolorsyncprofileuserdomain.md)
  The profile domain for the current user’s profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileuninstall(_:_:))*