# ColorSyncProfileCreateMutable()

**Framework**: ColorSync  
**Kind**: func

Creates an empty mutable profile.

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
func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?
```

#### Return Value

An empty mutable profile, or `NULL` in case of failure.

## See Also

- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithname(_:).md)
  Creates a profile from a predefined profile name.
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurl(_:_:).md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurlandoptions(_:_:_:).md)
  Creates a profile from ICC profile data at a URL, using the given options.
- [func ColorSyncProfileCreateMutableCopy(ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutablecopy(_:).md)
  Creates a mutable copy of a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatemutable())*