# vDSP_destroy_fftsetupD

**Framework**: Accelerate  
**Kind**: func

Deallocates an existing double-precision FFT setup structure.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_destroy_fftsetupD(FFTSetupD __setup);
```

#### Discussion

`vDSP_destroy_fftsetup` frees existing setup data and releases any allocated memory.

## Parameters

- `__setup`: The setup structure to deallocate, previously created by  .

## See Also

- [vDSP_create_fftsetup](vdsp_create_fftsetup.md)
  Returns a setup structure that contains precalculated data for single-precision FFT functions.
- [vDSP_create_fftsetupD](vdsp_create_fftsetupd.md)
  Returns a setup structure that contains precalculated data for double-precision FFT functions.
- [vDSP_destroy_fftsetup](vdsp_destroy_fftsetup.md)
  Deallocates an existing single-precision FFT setup structure.
- [vDSP_DFT_CreateSetup](vdsp_dft_createsetup.md)
- [typealias FFTSetup](fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTSetupD](fftsetupd.md)
  An opaque type that contains setup information for a double-precision FFT transform.
- [typealias FFTRadix](fftradix.md)
  The radix of the FFT decomposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_destroy_fftsetupd)*