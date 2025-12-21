# isOpaque

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the image is opaque.

**Availability**:
- macOS ?+

## Declaration

```swift
var isOpaque: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the image should be treated as fully opaque; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) to indicate the image may include some transparent regions.

Use this property to test whether an image representation completely covers the area within the rectangle given by the [`size`](nsimagerep/size.md) property.

The property value does not indicate whether the image has an alpha channel or if there is partial or complete transparency when drawing the image rep. Use the [`hasAlpha`](nsimagerep/hasalpha.md) property to determine if the image has an alpha channel.

## See Also

- [var bitsPerSample: Int](nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
- [var colorSpaceName: NSColorSpaceName](nsimagerep/colorspacename.md)
  The name of the color space used by the image data.
- [var hasAlpha: Bool](nsimagerep/hasalpha.md)
  A Boolean value that indicates whether the image data has an alpha channel.
- [var pixelsHigh: Int](nsimagerep/pixelshigh.md)
  The height of the image, measured in pixels.
- [var pixelsWide: Int](nsimagerep/pixelswide.md)
  The width of the image, measured in pixels.
- [var layoutDirection: NSImage.LayoutDirection](nsimagerep/layoutdirection.md)
  The layout direction for the image.
- [Device-Specific Value](device-specific-value.md)
  A constant that is used by image representations to denote an attribute whose value changes to match the display device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/isopaque)*