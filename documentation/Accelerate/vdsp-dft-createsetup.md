# vDSP_DFT_CreateSetup

**Framework**: Accelerate  
**Kind**: func

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
vDSP_DFT_Setup vDSP_DFT_CreateSetup(vDSP_DFT_Setup __Previous, vDSP_Length __Length);
```

## See Also

- [vDSP_create_fftsetup](vdsp_create_fftsetup.md)
  Returns a setup structure that contains precalculated data for single-precision FFT functions.
- [vDSP_create_fftsetupD](vdsp_create_fftsetupd.md)
  Returns a setup structure that contains precalculated data for double-precision FFT functions.
- [vDSP_destroy_fftsetup](vdsp_destroy_fftsetup.md)
  Deallocates an existing single-precision FFT setup structure.
- [vDSP_destroy_fftsetupD](vdsp_destroy_fftsetupd.md)
  Deallocates an existing double-precision FFT setup structure.
- [typealias FFTSetup](fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTSetupD](fftsetupd.md)
  An opaque type that contains setup information for a double-precision FFT transform.
- [typealias FFTRadix](fftradix.md)
  The radix of the FFT decomposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_createsetup)*