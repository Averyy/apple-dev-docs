# alphaFirst

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A format where the alpha value comes first.

**Availability**:
- macOS

## Declaration

```swift
static var alphaFirst: NSBitmapImageRep.Format { get }
```

```c
NSBitmapFormatAlphaFirst
```

#### Discussion

If this option is not specified, alpha values are the last component specified, as in CMYKA and RGBA.

## See Also

### Constants
- [static var alphaNonpremultiplied: NSBitmapImageRep.Format](./alphanonpremultiplied.md)
  A format where alpha values are not premultiplied.
- [static var floatingPointSamples: NSBitmapImageRep.Format](./floatingpointsamples.md)
  A format where samples are specified using floating-point numbers.
- [static var sixteenBitBigEndian: NSBitmapImageRep.Format](./sixteenbitbigendian.md)
  A 16-bit, big endian format.
- [static var sixteenBitLittleEndian: NSBitmapImageRep.Format](./sixteenbitlittleendian.md)
  A 16-bit, little endian format.
- [static var thirtyTwoBitBigEndian: NSBitmapImageRep.Format](./thirtytwobitbigendian.md)
  A 32-bit, big endian format.
- [static var thirtyTwoBitLittleEndian: NSBitmapImageRep.Format](./thirtytwobitlittleendian.md)
  A 32-bit, little endian format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/format/alphafirst)*