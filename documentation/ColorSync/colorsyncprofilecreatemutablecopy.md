# ColorSyncProfileCreateMutableCopy(_:)

**Framework**: ColorSync  
**Kind**: func

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

#### Return Value

A new mutable profile, or `NULL` in case of failure.

## Parameters

- `prof`: The profile whose data the function copies into the new mutable profile.

## See Also

- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithname(_:).md)
  Creates a profile from a predefined profile name.
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurl(_:_:).md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurlandoptions(_:_:_:).md)
  Creates a profile from ICC profile data at a URL, using the given options.
- [func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutable().md)
  Creates an empty mutable profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatemutablecopy(_:))*