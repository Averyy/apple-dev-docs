# hasAlpha

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the image data has an alpha channel.

**Availability**:
- macOS

## Declaration

```swift
var hasAlpha: Bool { get set }
```

```objc
@property (getter=hasAlpha) BOOL alpha;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the receiver has a known alpha channel; otherwise, [`false`](../../Swift/false.md).

Subclasses can set this property when loading image data to notify the parent class whether that data contains an alpha component. Specifying a value of [`true`](../../Swift/true.md) does not add an alpha channel to the image data itself; it merely records the fact that the data has an alpha channel.

## See Also

### Specifying Information About the Representation
- [var bitsPerSample: Int](./bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
- [var colorSpaceName: NSColorSpaceName](./colorspacename.md)
  The name of the color space used by the image data.
- [var isOpaque: Bool](./isopaque.md)
  A Boolean value that indicates whether the image is opaque.
- [var pixelsHigh: Int](./pixelshigh.md)
  The height of the image, measured in pixels.
- [var pixelsWide: Int](./pixelswide.md)
  The width of the image, measured in pixels.
- [var layoutDirection: NSImage.LayoutDirection](./layoutdirection.md)
  The layout direction for the image.
- [Device-Specific Value](../device-specific-value.md)
  A constant that is used by image representations to denote an attribute whose value changes to match the display device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/hasalpha)*