# layoutDirection

**Framework**: AppKit  
**Kind**: property

The layout direction for the image.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var layoutDirection: NSImage.LayoutDirection { get set }
```

#### Discussion

For possible values, see [`NSImage.LayoutDirection`](nsimage/layoutdirection.md). The default value for new image representation objects is [`NSImage.LayoutDirection.unspecified`](nsimage/layoutdirection/unspecified.md).

## See Also

- [var bitsPerSample: Int](nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
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
- [Device-Specific Value](device-specific-value.md)
  A constant that is used by image representations to denote an attribute whose value changes to match the display device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/layoutdirection)*