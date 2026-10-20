# ColorSyncTransformCreate(_:_:)

**Framework**: ColorSync  
**Kind**: func  
**Role**: Function

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

```c
extern ColorSyncTransformRefColorSyncTransformCreate(CFArrayRef profileSequence, CFDictionaryRef options);
```

#### Return Value

A new [`ColorSyncTransform`](./colorsynctransform.md), or `NULL` in case of failure.

#### Discussion

Each dictionary in `profileSequence` contains a profile object and information on the usage of the profile in the transform.

Required keys:

- [`kColorSyncProfile`](./kcolorsyncprofile.md): A [`ColorSyncProfile`](./colorsyncprofile.md).
- [`kColorSyncRenderingIntent`](./kcolorsyncrenderingintent.md): A `CFStringRef` defining the rendering intent.
- [`kColorSyncTransformTag`](./kcolorsynctransformtag.md): A `CFStringRef` defining which tags to use.

Optional key:

- [`kColorSyncBlackPointCompensation`](./kcolorsyncblackpointcompensation.md): A `CFBooleanRef` to enable or disable black point compensation.

## Parameters

- `profileSequence`: An array of dictionaries, each one containing a profile object and the information on the usage of the profile in the transform.
- `options`: A dictionary with additional public global options (for example, preferred CMM, quality, and so on). It can also contain custom options that are CMM specific.

## See Also

### Creating and applying a transform
- [func ColorSyncTransformConvert(ColorSyncTransform!, Int, Int, UnsafeMutableRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, UnsafeRawPointer!, ColorSyncDataDepth, ColorSyncDataLayout, Int, CFDictionary?) -> Bool](./colorsynctransformconvert%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Converts color data from a source layout to a destination layout using a color transform.
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](./colorsynctransformgetprofilesequence%28_%29.md)
  Returns the profile sequence used to create a color transform.
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](./colorsynctransformcopyproperty%28_,_,_%29.md)
  Copies a property from a color transform.
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](./colorsynctransformsetproperty%28_,_,_%29.md)
  Sets a property on a color transform.
- [func ColorSyncTransformGetTypeID() -> CFTypeID](./colorsynctransformgettypeid%28%29.md)
  Returns the type identifier for the `ColorSyncTransform` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynctransformcreate(_:_:))*