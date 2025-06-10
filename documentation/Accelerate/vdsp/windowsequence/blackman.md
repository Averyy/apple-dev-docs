# vDSP.WindowSequence.blackman

**Framework**: Accelerate  
**Kind**: case

The Blackman window, used to reduce spectral leakage prior to discrete Fourier transform.

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
case blackman
```

## Mentions

- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)

## See Also

- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [vDSP_blkman_window](vdsp_blkman_window.md)
  Creates a single-precision Blackman window.
- [vDSP_blkman_windowD](vdsp_blkman_windowd.md)
  Creates a double-precision Blackman window.
- [vDSP.WindowSequence.hamming](vdsp/windowsequence/hamming.md)
  The Hamming window, used to reduce spectral leakage prior to discrete Fourier transform.
- [vDSP.WindowSequence.hanningDenormalized](vdsp/windowsequence/hanningdenormalized.md)
  The denormalized-Hann window, used to reduce spectral leakage prior to discrete Fourier transform.
- [vDSP.WindowSequence.hanningNormalized](vdsp/windowsequence/hanningnormalized.md)
  The normalized-Hann window, used to reduce spectral leakage prior to discrete Fourier transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/windowsequence/blackman)*