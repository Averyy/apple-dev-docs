# samplesPerPixel

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of components for each pixel.

**Availability**:
- macOS

## Declaration

```swift
var samplesPerPixel: Int { get }
```

```objc
@property (readonly) NSInteger samplesPerPixel;
```

## Discussion

This property reflects both the number of color components and the coverage component, if present.

## See Also

### Related Documentation
- [var bitsPerSample: Int](../nsimagerep/bitspersample.md)
  The number of bits per sample in the object (if the object is a planar image, this property contains the number of bits per sample per plane).
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
- [var isPlanar: Bool](./isplanar.md)
  A Boolean value that indicates whether the image data is in a planar configuration.
- [var numberOfPlanes: Int](./numberofplanes.md)
  The number of separate planes into which the image data is organized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/samplesperpixel)*