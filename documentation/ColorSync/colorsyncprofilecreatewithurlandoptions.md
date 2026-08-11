# ColorSyncProfileCreateWithURLAndOptions(_:_:_:)

**Framework**: ColorSync  
**Kind**: func

Creates a profile from ICC profile data at a URL, using the given options.

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
func ColorSyncProfileCreateWithURLAndOptions(_ url: CFURL!, _ options: CFDictionary?, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?
```

#### Return Value

A new profile, or `NULL` in case of failure.

## Parameters

- `url`: The URL to the profile data.
- `options`: A dictionary with creation options, for example [`kColorSyncDoNotSubstituteProfiles`](kcolorsyncdonotsubstituteprofiles.md).
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithname(_:).md)
  Creates a profile from a predefined profile name.
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurl(_:_:).md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutable().md)
  Creates an empty mutable profile.
- [func ColorSyncProfileCreateMutableCopy(ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutablecopy(_:).md)
  Creates a mutable copy of a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatewithurlandoptions(_:_:_:))*