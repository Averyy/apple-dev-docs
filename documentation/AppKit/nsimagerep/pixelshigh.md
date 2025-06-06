# pixelsHigh

**Framework**: AppKit  
**Kind**: property

The height of the image, measured in pixels.

**Availability**:
- macOS ?+

## Declaration

```swift
var pixelsHigh: Int { get set }
```

#### Discussion

The value of this property is the height of the image, measured in the units of the device coordinate space. This value is usually derived from the image data itself.

Subclasses can use this property when loading image data to notify the parent class of the image height. Setting this property does not change the actual number of pixels in the image.

## See Also

- [var NSImageRepMatchesDevice: Int](nsimagerepmatchesdevice.md)
  A constant indicating that the value of certain attributes, such as the number of colors or bits per sample, will change to match the display device.
- [var size: NSSize](nsimagerep/size.md)
  The size of the image representation, measured in points in the user coordinate space.
- [var bitsPerSample: Int](nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
- [var colorSpaceName: NSColorSpaceName](nsimagerep/colorspacename.md)
  The name of the color space used by the image data.
- [var hasAlpha: Bool](nsimagerep/hasalpha.md)
  A Boolean value that indicates whether the image data has an alpha channel.
- [var isOpaque: Bool](nsimagerep/isopaque.md)
  A Boolean value that indicates whether the image is opaque.
- [var pixelsWide: Int](nsimagerep/pixelswide.md)
  The width of the image, measured in pixels.
- [var layoutDirection: NSImage.LayoutDirection](nsimagerep/layoutdirection.md)
  The layout direction for the image.
- [Device-Specific Value](device-specific-value.md)
  A constant that is used by image representations to denote an attribute whose value changes to match the display device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/pixelshigh)*