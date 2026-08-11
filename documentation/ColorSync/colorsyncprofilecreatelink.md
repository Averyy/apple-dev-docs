# ColorSyncProfileCreateLink(_:_:)

**Framework**: ColorSync  
**Kind**: func

Creates a device link profile from an array of profiles.

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
func ColorSyncProfileCreateLink(_ profileInfo: CFArray!, _ options: CFDictionary?) -> Unmanaged<ColorSyncProfile>?
```

#### Return Value

A new profile, or `NULL` in case of failure.

#### Discussion

Each dictionary in `profileInfo` contains a profile object and information on the usage of the profile in the transform.

Required keys:

- [`kColorSyncProfile`](kcolorsyncprofile.md): A [`ColorSyncProfile`](colorsyncprofile.md).
- [`kColorSyncRenderingIntent`](kcolorsyncrenderingintent.md): A `CFStringRef` defining the rendering intent.
- [`kColorSyncTransformTag`](kcolorsynctransformtag.md): A `CFStringRef` defining which tags to use.

Optional key:

- [`kColorSyncBlackPointCompensation`](kcolorsyncblackpointcompensation.md): A `CFBooleanRef` to enable or disable black point compensation.

## Parameters

- `profileInfo`: An array of dictionaries, each containing a profile object and the information on the usage of the profile in the transform.
- `options`: A dictionary with additional public global options (for example, preferred CMM, quality, and so on). It can also contain custom options that are CMM specific.

## See Also

- [var kColorSyncTransformDeviceToDevice: Unmanaged<CFString>!](kcolorsynctransformdevicetodevice.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value selecting the device-to-device conversion direction.
- [var kColorSyncTransformGamutCheck: Unmanaged<CFString>!](kcolorsynctransformgamutcheck.md)
  A [`kColorSyncTransformTag`](kcolorsynctransformtag.md) value that checks whether colors fall outside the destination gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsyncprofilecreatelink(_:_:))*