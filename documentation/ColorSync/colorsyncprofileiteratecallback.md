# ColorSyncProfileIterateCallback

**Framework**: ColorSync  
**Kind**: typealias  
**Role**: Type Alias

A callback that the framework invokes for each installed profile during iteration.

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
typealias ColorSyncProfileIterateCallback = (CFDictionary?, UnsafeMutableRawPointer?) -> Bool
```

```c
typedef _Bool (*)(const struct __CFDictionary *, void *) ColorSyncProfileIterateCallback;
```

## Discussion

The framework passes only validated profiles to the callback. Return `false` to stop the iteration.

## Parameters

- `profileInfo`: A dictionary describing the profile.
- `userInfo`: The user info passed to the iteration function.

## See Also

### Finding installed profiles
- [func ColorSyncIterateInstalledProfiles(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](./colorsynciterateinstalledprofiles%28_,_,_,_%29.md)
  Iterates over the installed profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileiteratecallback)*