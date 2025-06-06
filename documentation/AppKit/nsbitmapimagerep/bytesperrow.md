# bytesPerRow

**Framework**: AppKit  
**Kind**: property

The minimum number of bytes required to specify a scan line in each data plane.

**Availability**:
- macOS ?+

## Declaration

```swift
var bytesPerRow: Int { get }
```

#### Discussion

A scan line is a single row of pixels spanning the width of the image. If not explicitly set to another value (in [`init(bitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:)`](nsbitmapimagerep/init(bitmapdataplanes:pixelswide:pixelshigh:bitspersample:samplesperpixel:hasalpha:isplanar:colorspacename:bytesperrow:bitsperpixel:).md)), this number will be figured from the width of the image, the number of bits per sample, and, if the data is in a meshed configuration, the number of samples per pixel. It can be set to another value to indicate that each row of data is aligned on word or other boundaries.

## See Also

- [var bitmapFormat: NSBitmapImageRep.Format](nsbitmapimagerep/bitmapformat.md)
  The format of the bitmap image representation.
- [NSBitmapImageRep.Format](nsbitmapimagerep/format.md)
  Constants that represent bitmap component formats.
- [var bitsPerPixel: Int](nsbitmapimagerep/bitsperpixel.md)
  The number of bits allocated for each pixel in each plane of data.
- [var bytesPerPlane: Int](nsbitmapimagerep/bytesperplane.md)
  The number of bytes in each plane or channel of data.
- [var isPlanar: Bool](nsbitmapimagerep/isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var numberOfPlanes: Int](nsbitmapimagerep/numberofplanes.md)
  The number of separate planes into which the image data is organized.
- [var samplesPerPixel: Int](nsbitmapimagerep/samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/bytesperrow)*