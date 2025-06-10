# vDSP.WindowSequence.hanningNormalized

**Framework**: Accelerate  
**Kind**: case

The normalized-Hann window, used to reduce spectral leakage prior to discrete Fourier transform.

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
case hanningNormalized
```

## See Also

- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [vDSP_hann_window](vdsp_hann_window.md)
  Creates a single-precision Hann window.
- [vDSP_hann_windowD](vdsp_hann_windowd.md)
  Creates a double-precision Hann window.
- [vDSP.WindowSequence.blackman](vdsp/windowsequence/blackman.md)
  The Blackman window, used to reduce spectral leakage prior to discrete Fourier transform.
- [vDSP.WindowSequence.hamming](vdsp/windowsequence/hamming.md)
  The Hamming window, used to reduce spectral leakage prior to discrete Fourier transform.
- [vDSP.WindowSequence.hanningDenormalized](vdsp/windowsequence/hanningdenormalized.md)
  The denormalized-Hann window, used to reduce spectral leakage prior to discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/windowsequence/hanningnormalized)*