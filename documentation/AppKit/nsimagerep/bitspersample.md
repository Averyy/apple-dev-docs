# bitsPerSample

**Framework**: AppKit  
**Kind**: property

The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).

**Availability**:
- macOS ?+

## Declaration

```swift
var bitsPerSample: Int { get set }
```

#### Discussion

The number of bits used to specify each component of data in a single pixel (for example, a value of 8 for an RGBA image means that each pixel is comprised of four 8-bit values) or [`NSImageRepMatchesDevice`](nsimagerepmatchesdevice.md).

A subclass can set this property when loading image data to notify the parent class of how many bits each sample uses. Specifying a value that differs from the actual image data does not change the bit depth of the image.

## See Also

- [var bitsPerPixel: Int](nsbitmapimagerep/bitsperpixel.md)
  The number of bits allocated for each pixel in each plane of data.
- [var samplesPerPixel: Int](nsbitmapimagerep/samplesperpixel.md)
  The number of components for each pixel.
- [var isPlanar: Bool](nsbitmapimagerep/isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var colorSpaceName: NSColorSpaceName](nsimagerep/colorspacename.md)
  The name of the color space used by the image data.
- [var hasAlpha: Bool](nsimagerep/hasalpha.md)
  A Boolean value that indicates whether the image data has an alpha channel.
- [var isOpaque: Bool](nsimagerep/isopaque.md)
  A Boolean value that indicates whether the image is opaque.
- [var pixelsHigh: Int](nsimagerep/pixelshigh.md)
  The height of the image, measured in pixels.
- [var pixelsWide: Int](nsimagerep/pixelswide.md)
  The width of the image, measured in pixels.
- [var layoutDirection: NSImage.LayoutDirection](nsimagerep/layoutdirection.md)
  The layout direction for the image.
- [Device-Specific Value](device-specific-value.md)
  A constant that is used by image representations to denote an attribute whose value changes to match the display device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/bitspersample)*