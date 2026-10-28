# FFTRadix

**Framework**: Accelerate  
**Kind**: typealias  
**Role**: Type Alias

The radix of the FFT decomposition.

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
typealias FFTRadix = Int32
```

```c
typedef int FFTRadix;
```

## Discussion

Pass an `FFTRadix` value as an argument to [`vDSP_create_fftsetup`](../kernel/api-1580009-vdsp_create_fftsetup.md) or [`vDSP_create_fftsetupD`](./vdsp_create_fftsetupd.md).

## See Also

### FFT Setup
- [typealias FFTSetup](./fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTSetupD](./fftsetupd.md)
  An opaque type that contains setup information for a double-precision FFT transform.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fftradix)*