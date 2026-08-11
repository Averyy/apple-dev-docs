# ColorSyncTransformConvert(_:_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: ColorSync  
**Kind**: func

Converts color data from a source layout to a destination layout using a color transform.

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
func ColorSyncTransformConvert(_ transform: ColorSyncTransform!, _ width: Int, _ height: Int, _ dst: UnsafeMutableRawPointer!, _ dstDepth: ColorSyncDataDepth, _ dstLayout: ColorSyncDataLayout, _ dstBytesPerRow: Int, _ src: UnsafeRawPointer!, _ srcDepth: ColorSyncDataDepth, _ srcLayout: ColorSyncDataLayout, _ srcBytesPerRow: Int, _ options: CFDictionary?) -> Bool
```

#### Return Value

`true` if the conversion succeeds, or `false` otherwise.

#### Discussion

Use this function with care for performance reasons. Color conversions are computationally intensive and the recommended way to perform these is by using the vImage converter with a ColorSync code fragment. vImage employs vectorized code which is not only faster but also more battery efficient. Please visit the following link to see a sample application of vImage used in conjunction with ColorSync: [`https://developer.apple.com/library/prerelease/content/samplecode/convertImage/Listings/convertImage_main_c.html`](https://developer.apple.comhttps://developer.apple.com/library/prerelease/content/samplecode/convertImage/Listings/convertImage_main_c.html) More details regarding ColorSync code fragments are included below, as well.

## Parameters

- `transform`: The transform to use for converting color.
- `width`: The width of the image in pixels.
- `height`: The height of the image in pixels.
- `dst`: A pointer to the destination where the function writes the results.
- `dstDepth`: Describes the bit depth and type of the destination color components.
- `dstLayout`: Describes the format and byte packing of the destination pixels.
- `dstBytesPerRow`: The number of bytes in the row of data.
- `src`: A pointer to the data to convert.
- `srcDepth`: Describes the bit depth and type of the source color components.
- `srcLayout`: Describes the format and byte packing of the source pixels.
- `srcBytesPerRow`: The number of bytes in the row of data.
- `options`: A dictionary with additional options.

## See Also

- [func ColorSyncTransformCreate(CFArray?, CFDictionary?) -> Unmanaged<ColorSyncTransform>?](colorsynctransformcreate(_:_:).md)
  Creates a color transform from a sequence of profiles.
- [func ColorSyncTransformGetProfileSequence(ColorSyncTransform!) -> Unmanaged<CFArray>?](colorsynctransformgetprofilesequence(_:).md)
  Returns the profile sequence used to create a color transform.
- [func ColorSyncTransformCopyProperty(ColorSyncTransform!, CFTypeRef!, CFDictionary?) -> Unmanaged<CFTypeRef>?](colorsynctransformcopyproperty(_:_:_:).md)
  Copies a property from a color transform.
- [func ColorSyncTransformSetProperty(ColorSyncTransform!, CFTypeRef!, CFTypeRef?)](colorsynctransformsetproperty(_:_:_:).md)
  Sets a property on a color transform.
- [func ColorSyncTransformGetTypeID() -> CFTypeID](colorsynctransformgettypeid().md)
  Returns the type identifier for the `ColorSyncTransform` opaque type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/colorsync/colorsynctransformconvert(_:_:_:_:_:_:_:_:_:_:_:_:))*