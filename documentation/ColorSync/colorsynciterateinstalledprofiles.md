# ColorSyncIterateInstalledProfiles(_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

Iterates over the installed profiles.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func ColorSyncIterateInstalledProfiles(_ callBack: ColorSyncProfileIterateCallback?, _ seed: UnsafeMutablePointer<UInt32>?, _ userInfo: UnsafeMutableRawPointer?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?)
```

#### Discussion

When called for the first time, this function returns only system profiles, because profile iteration is a slow process requiring multiple accesses to the file system. Clients are advised to register for [`kColorSyncProfileRepositoryChangeNotification`](kcolorsyncprofilerepositorychangenotification.md) using `CFNotificationCenter` or `NSNotificationCenter` to obtain all installed profiles. The notification callback receives, if possible, a `CFDictionary` containing a new seed value of the profile cache (key [`kColorSyncProfileCacheSeed`](kcolorsyncprofilecacheseed.md) / value `kCFNumberSInt32Type`). Comparing old and new seed values may prevent unnecessary calls to iterate installed profiles. Alternatively, call [`ColorSyncIterateInstalledProfilesWithOptions(_:_:_:_:_:)`](colorsynciterateinstalledprofileswithoptions(_:_:_:_:_:).md) with the [`kColorSyncWaitForCacheReply`](kcolorsyncwaitforcachereply.md) option set to `kCFBooleanTrue` to obtain all installed profiles in one call.

## Parameters

- `callBack`: A pointer to a client-provided function (can be `NULL`).
- `seed`: A pointer to a cache seed owned by the client (can be `NULL`).
- `userInfo`: User-defined data passed to the callback.
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

- [typealias ColorSyncProfileIterateCallback](colorsyncprofileiteratecallback.md)
  A callback that the framework invokes for each installed profile during iteration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynciterateinstalledprofiles(_:_:_:_:))*