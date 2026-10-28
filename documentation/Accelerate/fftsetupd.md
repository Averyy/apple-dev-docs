# FFTSetupD

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

An opaque type that contains setup information for a double-precision FFT transform.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias FFTSetupD = OpaquePointer
```

```c
typedef struct OpaqueFFTSetupD * FFTSetupD;
```

## Discussion

Call the [`vDSP_create_fftsetupD`](./vdsp_create_fftsetupd.md) function to create a setup structure, and calll [`vDSP_destroy_fftsetupD`](./vdsp_destroy_fftsetupd.md) to deallocate a setup structure.

## See Also

### FFT Setup
- [typealias FFTSetup](./fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTRadix](./fftradix.md)
  The radix of the FFT decomposition.
- [vDSP_create_fftsetup](./vdsp_create_fftsetup.md)
  Returns a setup structure that contains precalculated data for single-precision FFT functions.
- [vDSP_create_fftsetupD](./vdsp_create_fftsetupd.md)
  Returns a setup structure that contains precalculated data for double-precision FFT functions.
- [vDSP_destroy_fftsetup](./vdsp_destroy_fftsetup.md)
  Deallocates an existing single-precision FFT setup structure.
- [vDSP_destroy_fftsetupD](./vdsp_destroy_fftsetupd.md)
  Deallocates an existing double-precision FFT setup structure.
- [vDSP_DFT_CreateSetup](./vdsp_dft_createsetup.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fftsetupd)*