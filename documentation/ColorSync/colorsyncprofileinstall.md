# ColorSyncProfileInstall(_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

Installs a profile in the specified domain.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncProfileInstall(_ profile: ColorSyncProfile!, _ domain: CFString!, _ subpath: CFString!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool
```

#### Return Value

`true` on success, or `false` in case of error.

#### Discussion

The `domain` is either [`kColorSyncProfileComputerDomain`](kcolorsyncprofilecomputerdomain.md) or [`kColorSyncProfileUserDomain`](kcolorsyncprofileuserdomain.md). [`kColorSyncProfileComputerDomain`](kcolorsyncprofilecomputerdomain.md) is for sharing the profiles (from `/Library/ColorSync/Profiles`). [`kColorSyncProfileUserDomain`](kcolorsyncprofileuserdomain.md) is for user custom profiles (installed under the home directory, that is, in `~/Library/ColorSync/Profiles`). `NULL` is the same as [`kColorSyncProfileUserDomain`](kcolorsyncprofileuserdomain.md).

The `subpath` is the file system representation of the path of the file to contain the installed profile. The function interprets the last component of the path as a file name if it ends with the extension `.icc`. Otherwise, the function interprets the subpath as the directory path and creates the file name from the profile description tag, appended with the `.icc` extension.

Using this function requires `COLORSYNC_PROFILE_INSTALL_ENTITLEMENT`.

## Parameters

- `profile`: The profile to install.
- `domain`: The domain to install into, either [`kColorSyncProfileComputerDomain`](kcolorsyncprofilecomputerdomain.md) or [`kColorSyncProfileUserDomain`](kcolorsyncprofileuserdomain.md).
- `subpath`: A string created from the file system representation of the path of the file to contain the installed profile.
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

- [func ColorSyncProfileUninstall(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileuninstall(_:_:).md)
  Uninstalls a profile.
- [func ColorSyncIterateInstalledProfilesWithOptions(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:).md)
  Iterates over the installed profiles, using the given options.
- [var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String](colorsync_profile_install_entitlement.md)
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](kcolorsyncprofilecomputerdomain.md)
  The profile domain for profiles shared by all users of the computer.
- [var kColorSyncProfileUserDomain: Unmanaged<CFString>!](kcolorsyncprofileuserdomain.md)
  The profile domain for the current user’s profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileinstall(_:_:_:_:))*