# ColorSyncTransformCreate(_:_:)

**Framework**: ColorSync  
**Kind**: func

Creates a color transform from a sequence of profiles.

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
func ColorSyncTransformCreate(_ profileSequence: CFArray?, _ options: CFDictionary?) -> Unmanaged<ColorSyncTransform>?
```

#### Return Value

A new [`ColorSyncTransform`](colorsynctransform.md), or `NULL` in case of failure.

#### Discussion

Each dictionary in `profileSequence` contains a profile object and information on the usage of the profile in the transform.

Required keys:

- [`kColorSyncProfile`](kcolorsyncprofile.md): A [`ColorSyncProfile`](colorsyncprofile.md).
- [`kColorSyncRenderingIntent`](kcolorsyncrenderingintent.md): A `CFStringRef` defining the rendering intent.
- [`kColorSyncTransformTag`](kcolorsynctransformtag.md): A `CFStringRef` defining which tags to use.

Optional key:

- [`kColorSyncBlackPointCompensation`](kcolorsyncblackpointcompensation.md): A `CFBooleanRef` to enable or disable black point compensation.

## Parameters

- `profileSequence`: An array of dictionaries, each one containing a profile object and the information on the usage of the profile in the transform.
- `options`: A dictionary with additional public global options (for example, preferred CMM, quality, and so on). It can also contain custom options that are CMM specific.

## See Also

- [func ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutableRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafeRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool](colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Converts color data from a source layout to a destination layout using a color transform.
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](colorsynctransformgetprofilesequence(_:).md)
  Returns the profile sequence used to create a color transform.
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](colorsynctransformcopyproperty(_:_:_:).md)
  Copies a property from a color transform.
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](colorsynctransformsetproperty(_:_:_:).md)
  Sets a property on a color transform.
- [func ColorSyncTransformGetTypeID() -> CFTypeID](colorsynctransformgettypeid().md)
  Returns the type identifier for the `ColorSyncTransform` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynctransformcreate(_:_:))*