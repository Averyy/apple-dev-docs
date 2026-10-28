# ColorSyncProfileCreateWithURLAndOptions(_:_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

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

```c
extern ColorSyncProfileRefColorSyncProfileCreateWithURLAndOptions(CFURLRef url, CFDictionaryRef options, CFErrorRef*error);
```

## Return Value

A new profile, or `NULL` in case of failure.

## Parameters

- `url`: The URL to the profile data.
- `options`: A dictionary with creation options, for example [`kColorSyncDoNotSubstituteProfiles`](./kcolorsyncdonotsubstituteprofiles.md).
- `error`: On failure, a pointer to an error describing the problem. Optional.

## See Also

### Creating a profile
- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithname%28_%29.md)
  Creates a profile from a predefined profile name.
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithurl%28_,_%29.md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?](./colorsyncprofilecreatemutable%28%29.md)
  Creates an empty mutable profile.
- [func ColorSyncProfileCreateMutableCopy(ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?](./colorsyncprofilecreatemutablecopy%28_%29.md)
  Creates a mutable copy of a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatewithurlandoptions(_:_:_:))*