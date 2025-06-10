# NSBitmapImageRep.Format

**Framework**: AppKit  
**Kind**: struct

Constants that represent bitmap component formats.

**Availability**:
- macOS ?+

## Declaration

```swift
struct Format
```

#### Overview

You can combine these values and pass them to the  [`init(bitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:)`](nsbitmapimagerep/init(bitmapdataplanes:pixelswide:pixelshigh:bitspersample:samplesperpixel:hasalpha:isplanar:colorspacename:bitmapformat:bytesperrow:bitsperpixel:).md) method as the bitmap format. You can access them later in the  [`bitmapFormat`](nsbitmapimagerep/bitmapformat.md) property.

## Topics

### Constants
- [static var alphaFirst: NSBitmapImageRep.Format](nsbitmapimagerep/format/alphafirst.md)
  A format where the alpha value comes first.
- [static var alphaNonpremultiplied: NSBitmapImageRep.Format](nsbitmapimagerep/format/alphanonpremultiplied.md)
  A format where alpha values are not premultiplied.
- [static var floatingPointSamples: NSBitmapImageRep.Format](nsbitmapimagerep/format/floatingpointsamples.md)
  A format where samples are specified using floating-point numbers.
- [static var sixteenBitBigEndian: NSBitmapImageRep.Format](nsbitmapimagerep/format/sixteenbitbigendian.md)
  A 16-bit, big endian format.
- [static var sixteenBitLittleEndian: NSBitmapImageRep.Format](nsbitmapimagerep/format/sixteenbitlittleendian.md)
  A 16-bit, little endian format.
- [static var thirtyTwoBitBigEndian: NSBitmapImageRep.Format](nsbitmapimagerep/format/thirtytwobitbigendian.md)
  A 32-bit, big endian format.
- [static var thirtyTwoBitLittleEndian: NSBitmapImageRep.Format](nsbitmapimagerep/format/thirtytwobitlittleendian.md)
  A 32-bit, little endian format.
### Initializers
- [init(rawValue: UInt)](nsbitmapimagerep/format/init(rawvalue:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var bitmapFormat: NSBitmapImageRep.Format](nsbitmapimagerep/bitmapformat.md)
  The format of the bitmap image representation.
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
- [var samplesPerPixel: Int](nsbitmapimagerep/samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/format)*