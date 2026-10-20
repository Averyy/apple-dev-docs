# isPlanar

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the image data is in a planar configuration.

**Availability**:
- macOS

## Declaration

```swift
var isPlanar: Bool { get }
```

```objc
@property (readonly, getter=isPlanar) BOOL planar;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the data is in a planar configuration or [`false`](../../Swift/false.md) if it is in a meshed configuration. In a planar configuration, the image data is segregated into a separate plane for each color and coverage component. In a meshed configuration, the data is integrated into a single plane.

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
- [var bytesPerRow: Int](./bytesperrow.md)
  The minimum number of bytes required to specify a scan line in each data plane.
- [var numberOfPlanes: Int](./numberofplanes.md)
  The number of separate planes into which the image data is organized.
- [var samplesPerPixel: Int](./samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/isplanar)*