# ColorSyncIterateInstalledProfilesWithOptions(_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

Iterates over the installed profiles, using the given options.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.13+

## Declaration

```swift
func ColorSyncIterateInstalledProfilesWithOptions(_ callBack: ColorSyncProfileIterateCallback?, _ seed: UnsafeMutablePointer<UInt32>?, _ userInfo: UnsafeMutableRawPointer?, _ options: CFDictionary?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?)
```

## Parameters

- `callBack`: A pointer to a client-provided function (can be `NULL`).
- `seed`: A pointer to a cache seed owned by the client.
- `userInfo`: User-defined data passed to the callback.
- `options`: A dictionary with iteration options, for example [`kColorSyncWaitForCacheReply`](kcolorsyncwaitforcachereply.md) to wait for the cache to finish updating before returning.
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

- [func ColorSyncProfileInstall(ColorSyncProfile!, CFString!, CFString!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileinstall(_:_:_:_:).md)
  Installs a profile in the specified domain.
- [func ColorSyncProfileUninstall(ColorSyncProfile!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Bool](colorsyncprofileuninstall(_:_:).md)
  Uninstalls a profile.
- [var COLORSYNC_PROFILE_INSTALL_ENTITLEMENT: String](colorsync_profile_install_entitlement.md)
- [var kColorSyncProfileComputerDomain: Unmanaged<CFString>!](kcolorsyncprofilecomputerdomain.md)
  The profile domain for profiles shared by all users of the computer.
- [var kColorSyncProfileUserDomain: Unmanaged<CFString>!](kcolorsyncprofileuserdomain.md)
  The profile domain for the current user’s profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:))*