# ColorSyncProfileCreateWithName(_:)

**Framework**: ColorSync  
**Kind**: func

Creates a profile from a predefined profile name.

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
func ColorSyncProfileCreateWithName(_ name: CFString!) -> Unmanaged<ColorSyncProfile>?
```

#### Return Value

A new profile, or `NULL` in case of failure.

## Parameters

- `name`: The predefined profile name.

## See Also

- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurl(_:_:).md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](colorsyncprofilecreatewithurlandoptions(_:_:_:).md)
  Creates a profile from ICC profile data at a URL, using the given options.
- [func ColorSyncProfileCreateMutable() -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutable().md)
  Creates an empty mutable profile.
- [func ColorSyncProfileCreateMutableCopy(ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?](colorsyncprofilecreatemutablecopy(_:).md)
  Creates a mutable copy of a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatewithname(_:))*