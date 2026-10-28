# colorSpaceName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the color space used by the image data.

**Availability**:
- macOS

## Declaration

```swift
var colorSpaceName: NSColorSpaceName { get set }
```

```objc
@property (copy) NSColorSpaceName colorSpaceName;
```

## Discussion

By default, an `NSImageRep` object’s color space name is `NSCalibratedRGBColorSpace`. Color space names are defined as part of the `NSColor` class, in `NSGraphics.h`. The following are valid color space names:

- `NSCalibratedWhiteColorSpace`
- `NSCalibratedBlackColorSpace`
- `NSCalibratedRGBColorSpace`
- `NSDeviceWhiteColorSpace`
- `NSDeviceBlackColorSpace`
- `NSDeviceRGBColorSpace`
- `NSDeviceCMYKColorSpace`
- `NSNamedColorSpace`
- `NSCustomColorSpace`

## See Also

### Specifying Information About the Representation
- [var bitsPerSample: Int](./bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
- [var hasAlpha: Bool](./hasalpha.md)
  A Boolean value that indicates whether the image data has an alpha channel.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/colorspacename)*