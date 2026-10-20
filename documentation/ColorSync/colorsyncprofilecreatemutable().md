# ColorSyncProfileCreateMutable()

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

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

```c
extern ColorSyncMutableProfileRefColorSyncProfileCreateMutable();
```

#### Return Value

An empty mutable profile, or `NULL` in case of failure.

## See Also

### Creating a profile
- [func ColorSyncProfileCreateWithName(CFString!) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithname%28_%29.md)
  Creates a profile from a predefined profile name.
- [func ColorSyncProfileCreateWithURL(CFURL!, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithurl%28_,_%29.md)
  Creates a profile from ICC profile data at a URL.
- [func ColorSyncProfileCreateWithURLAndOptions(CFURL!, CFDictionary?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatewithurlandoptions%28_,_,_%29.md)
  Creates a profile from ICC profile data at a URL, using the given options.
- [func ColorSyncProfileCreateMutableCopy(ColorSyncProfile!) -> Unmanaged<ColorSyncMutableProfile>?](./colorsyncprofilecreatemutablecopy%28_%29.md)
  Creates a mutable copy of a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatemutable())*