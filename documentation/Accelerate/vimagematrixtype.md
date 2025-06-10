# vImageMatrixType

**Framework**: Accelerate  
**Kind**: typealias

An enumeration of RGB -> Y’CbCr conversion matrix types.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
typealias vImageMatrixType = UInt32
```

#### Discussion

Currently, only one matrix type is available. Additional formats are reserved for future expansion.

## Topics

### Constants
- [var kvImageMatrixType_ARGBToYpCbCrMatrix: Int](kvimagematrixtype_argbtoypcbcrmatrix.md)
- [var kvImageMatrixType_None: Int](kvimagematrixtype_none.md)

## See Also

- [Error codes](1578972-error-codes.md)
  Error codes that vImage functions return when an operation fails.
- [Core Video Image Format Errors](1498271-core-video-image-format-errors.md)
- [Processing Flags](1578976-processing-flags.md)
  Set flags on vImage operations to specify processing options.
- [Dithering Methods](1533233-dithering-methods.md)
  Specify the dithering method some vImage conversion functions use.
- [Availability Flags](availability-flags.md)
  Obtain the availability of particular vImage features.
- [Decode Arrays](decode-arrays.md)
  Specify the decode array constant to use with 16Q12-formatted data.
- [Buffer Types](buffer-types.md)
  Look up buffer type codes vImage conversions provide.
- [typealias vImage_WarpInterpolation](vimage_warpinterpolation.md)
  Constants for selecting the interpolation mode


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagematrixtype)*