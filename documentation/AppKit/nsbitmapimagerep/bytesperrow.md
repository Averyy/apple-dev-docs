# bytesPerRow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum number of bytes required to specify a scan line in each data plane.

**Availability**:
- macOS

## Declaration

```swift
var bytesPerRow: Int { get }
```

```objc
@property (readonly) NSInteger bytesPerRow;
```

#### Discussion

A scan line is a single row of pixels spanning the width of the image. If not explicitly set to another value (in [`init(bitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:)`](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bytesperrow,bitsperpixel%29.md)), this number will be figured from the width of the image, the number of bits per sample, and, if the data is in a meshed configuration, the number of samples per pixel. It can be set to another value to indicate that each row of data is aligned on word or other boundaries.

## See Also

### Getting Information About Images
- [var bitmapFormat: NSBitmapImageRep.Format](./bitmapformat.md)
  The format of the bitmap image representation.
- [NSBitmapImageRep.Format](./format.md)
  Constants that represent bitmap component formats.
- [var bitsPerPixel: Int](./bitsperpixel.md)
  The number of bits allocated for each pixel in each plane of data.
- [var bytesPerPlane: Int](./bytesperplane.md)
  The number of bytes in each plane or channel of data.
- [var isPlanar: Bool](./isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var numberOfPlanes: Int](./numberofplanes.md)
  The number of separate planes into which the image data is organized.
- [var samplesPerPixel: Int](./samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/bytesperrow)*