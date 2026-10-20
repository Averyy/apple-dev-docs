# ColorSyncProfileCreateMutableCopy(_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

Creates a mutable copy of a profile.

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
func ColorSyncProfileCreateMutableCopy(_ prof: ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?
```

```c
extern ColorSyncMutableProfileRefColorSyncProfileCreateMutableCopy(ColorSyncProfileRef prof);
```

#### Return Value

A new mutable profile, or `NULL` in case of failure.

## Parameters

- `prof`: The profile whose data the function copies into the new mutable profile.

## See Also

### Creating a profile
- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithname%28_%29.md)
  Creates a profile from a predefined profile name.
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithurl%28_,_%29.md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithurlandoptions%28_,_,_%29.md)
  Creates a profile from ICC profile data at a URL, using the given options.
- [func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?](./colorsyncprofilecreatemutable%28%29.md)
  Creates an empty mutable profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatemutablecopy(_:))*