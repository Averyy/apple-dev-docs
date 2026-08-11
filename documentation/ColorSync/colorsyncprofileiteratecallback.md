# ColorSyncProfileIterateCallback

**Framework**: ColorSync  
**Kind**: typealias

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

#### Discussion

The framework passes only validated profiles to the callback. Return `false` to stop the iteration.

## Parameters

- `profileInfo`: A dictionary describing the profile.
- `userInfo`: The user info passed to the iteration function.

## See Also

- [func ColorSyncIterateInstalledProfiles(ColorSyncProfileIterateCallback?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?, UnsafeMutablePointer<Unmanaged<CFError>?>?)](colorsynciterateinstalledprofiles(_:_:_:_:).md)
  Iterates over the installed profiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofileiteratecallback)*