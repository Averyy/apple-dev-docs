# isPlanar

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the image data is in a planar configuration.

**Availability**:
- macOS ?+

## Declaration

```swift
var isPlanar: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the data is in a planar configuration or [`false`](https://developer.apple.com/documentation/swift/false) if it is in a meshed configuration. In a planar configuration, the image data is segregated into a separate plane for each color and coverage component. In a meshed configuration, the data is integrated into a single plane.

## See Also

- [var bitmapFormat: NSBitmapImageRep.Format](nsbitmapimagerep/bitmapformat.md)
  The format of the bitmap image representation.
- [NSBitmapImageRep.Format](nsbitmapimagerep/format.md)
  Constants that represent bitmap component formats.
- [var bitsPerPixel: Int](nsbitmapimagerep/bitsperpixel.md)
  The number of bits allocated for each pixel in each plane of data.
- [var bytesPerPlane: Int](nsbitmapimagerep/bytesperplane.md)
  The number of bytes in each plane or channel of data.
- [var bytesPerRow: Int](nsbitmapimagerep/bytesperrow.md)
  The minimum number of bytes required to specify a scan line in each data plane.
- [var numberOfPlanes: Int](nsbitmapimagerep/numberofplanes.md)
  The number of separate planes into which the image data is organized.
- [var samplesPerPixel: Int](nsbitmapimagerep/samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/isplanar)*