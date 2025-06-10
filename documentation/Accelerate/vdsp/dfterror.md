# vDSP.DFTError

**Framework**: Accelerate  
**Kind**: enum

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
enum DFTError
```

## Topics

### Enumeration Cases
- [vDSP.DFTError.invalidInterleavedCount(count:)](vdsp/dfterror/invalidinterleavedcount(count:).md)
- [case invalidSplitComplexCount(count: Int, transformType: vDSP.DFTTransformType)](vdsp/dfterror/invalidsplitcomplexcount(count:transformtype:).md)
### Instance Properties
- [var errorDescription: String?](vdsp/dfterror/errordescription.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [vDSP.DCTTransformType](vdsp/dcttransformtype.md)
  An enumeration that describes the discrete cosine transform types.
- [vDSP.DFTTransformType](vdsp/dfttransformtype.md)
  Discrete Fourier transform types.
- [vDSP.FourierTransformDirection](vdsp/fouriertransformdirection.md)
  Fast Fourier transform directions.
- [vDSP.IntegrationRule](vdsp/integrationrule.md)
  Integration rules.
- [vDSP.Radix](vdsp/radix.md)
  Fast Fourier transform radices.
- [vDSP.RoundingMode](vdsp/roundingmode.md)
  Floating point to integer conversion rounding modes.
- [vDSP.SortOrder](vdsp/sortorder.md)
  Constants that specify the sorting order.
- [vDSP.ThresholdRule](vdsp/thresholdrule.md)
  Constants that specify vector threshold rules.
- [vDSP.WindowSequence](vdsp/windowsequence.md)
  Constants that specify window sequence functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/dfterror)*