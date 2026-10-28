# bytesPerPlane

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of bytes in each plane or channel of data.

**Availability**:
- macOS

## Declaration

```swift
var bytesPerPlane: Int { get }
```

```objc
@property (readonly) NSInteger bytesPerPlane;
```

## Discussion

This number is calculated from the number of bytes per row and the height of the image.

## See Also

### Getting Information About Images
- [var bitmapFormat: NSBitmapImageRep.Format](./bitmapformat.md)
  The format of the bitmap image representation.
- [NSBitmapImageRep.Format](./format.md)
  Constants that represent bitmap component formats.
- [var bitsPerPixel: Int](./bitsperpixel.md)
  The number of bits allocated for each pixel in each plane of data.
- [var bytesPerRow: Int](./bytesperrow.md)
  The minimum number of bytes required to specify a scan line in each data plane.
- [var isPlanar: Bool](./isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var numberOfPlanes: Int](./numberofplanes.md)
  The number of separate planes into which the image data is organized.
- [var samplesPerPixel: Int](./samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/bytesperplane)*