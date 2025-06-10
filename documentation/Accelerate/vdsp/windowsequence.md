# vDSP.WindowSequence

**Framework**: Accelerate  
**Kind**: enum

Constants that specify window sequence functions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
enum WindowSequence
```

## Topics

### Enumeration Cases
- [vDSP.WindowSequence.blackman](vdsp/windowsequence/blackman.md)
  The Blackman window, used to reduce spectral leakage prior to discrete Fourier transform.
- [vDSP.WindowSequence.hamming](vdsp/windowsequence/hamming.md)
  The Hamming window, used to reduce spectral leakage prior to discrete Fourier transform.
- [vDSP.WindowSequence.hanningDenormalized](vdsp/windowsequence/hanningdenormalized.md)
  The denormalized-Hann window, used to reduce spectral leakage prior to discrete Fourier transform.
- [vDSP.WindowSequence.hanningNormalized](vdsp/windowsequence/hanningnormalized.md)
  The normalized-Hann window, used to reduce spectral leakage prior to discrete Fourier transform.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

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
- [vDSP.DFTError](vdsp/dfterror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/windowsequence)*