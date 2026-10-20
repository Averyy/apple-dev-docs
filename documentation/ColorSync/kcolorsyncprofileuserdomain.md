# kColorSyncProfileUserDomain

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

The profile domain for the current user’s profiles.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
var kColorSyncProfileUserDomain: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncProfileUserDomain;
```

#### Discussion

On macOS, these profiles are in the `~/Library/ColorSync/Profiles` folder.

## See Also

### Installing profiles
- [func ColorSyncProfileInstall(ColorSyncProfile!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./colorsyncprofileinstall%28_,_,_,_%29.md)
  Installs a profile in the specified domain.
- [func ColorSyncProfileUninstall(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](./colorsyncprofileuninstall%28_,_%29.md)
  Uninstalls a profile.
- [func ColorSyncIterateInstalledProfilesWithOptions(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](./colorsynciterateinstalledprofileswithoptions%28_,_,_,_,_%29.md)
  Iterates over the installed profiles, using the given options.
- [var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String](./colorsync_profile_install_entitlement.md)
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](./kcolorsyncprofilecomputerdomain.md)
  The profile domain for profiles shared by all users of the computer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsyncprofileuserdomain)*