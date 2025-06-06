# samplesPerPixel

**Framework**: AppKit  
**Kind**: property

The number of components for each pixel.

**Availability**:
- macOS ?+

## Declaration

```swift
var samplesPerPixel: Int { get }
```

#### Discussion

This property reflects both the number of color components and the coverage component, if present.

## See Also

- [var bitsPerSample: Int](nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
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
- [var isPlanar: Bool](nsbitmapimagerep/isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var numberOfPlanes: Int](nsbitmapimagerep/numberofplanes.md)
  The number of separate planes into which the image data is organized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/samplesperpixel)*