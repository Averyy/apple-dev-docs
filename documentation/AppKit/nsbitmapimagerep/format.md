# NSBitmapImageRep.Format

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that represent bitmap component formats.

**Availability**:
- macOS

## Declaration

```swift
struct Format
```

```c
enum NSBitmapFormat : NSUInteger;
```

#### Overview

You can combine these values and pass them to the  [`init(bitmapDataPlanes:pixelsWide:pixelsHigh:bitsPerSample:samplesPerPixel:hasAlpha:isPlanar:colorSpaceName:bitmapFormat:bytesPerRow:bitsPerPixel:)`](./init%28bitmapdataplanes,pixelswide,pixelshigh,bitspersample,samplesperpixel,hasalpha,isplanar,colorspacename,bitmapformat,bytesperrow,bitsperpixel%29.md) method as the bitmap format. You can access them later in the  [`bitmapFormat`](./bitmapformat.md) property.

## Topics

### Constants
- [static var alphaFirst: NSBitmapImageRep.Format](./format/alphafirst.md)
  A format where the alpha value comes first.
- [static var alphaNonpremultiplied: NSBitmapImageRep.Format](./format/alphanonpremultiplied.md)
  A format where alpha values are not premultiplied.
- [static var floatingPointSamples: NSBitmapImageRep.Format](./format/floatingpointsamples.md)
  A format where samples are specified using floating-point numbers.
- [static var sixteenBitBigEndian: NSBitmapImageRep.Format](./format/sixteenbitbigendian.md)
  A 16-bit, big endian format.
- [static var sixteenBitLittleEndian: NSBitmapImageRep.Format](./format/sixteenbitlittleendian.md)
  A 16-bit, little endian format.
- [static var thirtyTwoBitBigEndian: NSBitmapImageRep.Format](./format/thirtytwobitbigendian.md)
  A 32-bit, big endian format.
- [static var thirtyTwoBitLittleEndian: NSBitmapImageRep.Format](./format/thirtytwobitlittleendian.md)
  A 32-bit, little endian format.
### Initializers
- [init(rawValue: UInt)](./format/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
### Deprecated
- [Deprecated symbols](../format-deprecated-symbols.md)
  Review symbols that are no longer in active development, and their recommended replacements.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Getting Information About Images
- [var bitmapFormat: NSBitmapImageRep.Format](./bitmapformat.md)
  The format of the bitmap image representation.
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
- [var samplesPerPixel: Int](./samplesperpixel.md)
  The number of components for each pixel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/format)*