# bitsPerPixel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of bits allocated for each pixel in each plane of data.

**Availability**:
- macOS

## Declaration

```swift
var bitsPerPixel: Int { get }
```

```objc
@property (readonly) NSInteger bitsPerPixel;
```

## Discussion

This number is normally equal to the number of bits per sample or, if the data is in meshed configuration, the number of bits per sample times the number of samples per pixel. It can be explicitly set to another value (in [`init(bitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bytesPerRow:bitsPerPixel:)`](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bytesperrow,bitsperpixel%29.md)) in case extra memory is allocated for each pixel. This may be the case, for example, if pixel data is aligned on byte boundaries.

## See Also

### Getting Information About Images
- [var bitmapFormat: NSBitmapImageRep.Format](./bitmapformat.md)
  The format of the bitmap image representation.
- [NSBitmapImageRep.Format](./format.md)
  Constants that represent bitmap component formats.
- [var bytesPerPlane: Int](./bytesperplane.md)
  The number of bytes in each plane or channel of data.
- [var bytesPerRow: Int](./bytesperrow.md)
  The minimum number of bytes required to specify a scan line in each data plane.
- [var isPlanar: Bool](./isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var numberOfPlanes: Int](./numberofplanes.md)
  The number of separate planes into which the image data is organized.
- [var samplesPerPixel: Int](./samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/bitsperpixel)*