# kColorSyncTransformDeviceToDevice

**Framework**: ColorSync  
**Kind**: var  
**Role**: Global Variable

A [`kColorSyncTransformTag`](./kcolorsynctransformtag.md) value selecting the device-to-device conversion direction.

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
var kColorSyncTransformDeviceToDevice: Unmanaged<CFString>!
```

```c
extern CFStringRef kColorSyncTransformDeviceToDevice;
```

## See Also

### Proofing and gamut checking
- [func ColorSyncProfileCreateLink(CFArray!, CFDictionary?) -> Unmanaged<ColorSyncProfile>?](./colorsyncprofilecreatelink%28_,_%29.md)
  Creates a device link profile from an array of profiles.
- [var kColorSyncTransformGamutCheck: Unmanaged<CFString>!](./kcolorsynctransformgamutcheck.md)
  A [`kColorSyncTransformTag`](./kcolorsynctransformtag.md) value that checks whether colors fall outside the destination gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/kcolorsynctransformdevicetodevice)*