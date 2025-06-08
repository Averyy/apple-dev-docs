# vDSP_create_fftsetupD

**Framework**: Accelerate  
**Kind**: func

Returns a setup structure that contains precalculated data for double-precision FFT functions.

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
extern FFTSetupD vDSP_create_fftsetupD(vDSP_Length __Log2n, FFTRadix __Radix);
```

#### Return Value

Returns an [`FFTSetup`](https://developer.apple.com/documentation/kernel/fftsetup) structure for use with FFT functions. Returns `0` on error.

#### Discussion

Use this function to create a weights array of complex exponential values that the vDSP FFT functions use for forward transforms. Precalculating these values during, for example, your app’s initialization, boosts FFT performance. You can use the same setup structure to perform transformations on vectors that contain up to `2`Log2n elements.

For 2D transformations, specify `Log2n` as the greater of the number of rows and the number of columns.

Call [`vDSP_destroy_fftsetup`](https://developer.apple.com/documentation/kernel/1579978-vdsp_destroy_fftsetup) to deallocate the setup structure.

> 💡 **Tip**:  To learn how the vDSP library scales and arranges the FFT output, see [`Understanding data packing for Fourier transforms`](understanding-data-packing-for-fourier-transforms.md).

## Parameters

- `__Log2n`: The base-two logarithm of the maximum number of elements the setup structure transforms. Subsequent calls to FFT functions using the resulting setup may transform this length or less.
- `__Radix`: Specifies radix options. This function only supports radix-2; other radices are deprecated. Use the   for radix-3, and radix-5.

## See Also

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [vDSP_create_fftsetup](vdsp_create_fftsetup.md)
  Returns a setup structure that contains precalculated data for single-precision FFT functions.
- [vDSP_destroy_fftsetup](vdsp_destroy_fftsetup.md)
  Deallocates an existing single-precision FFT setup structure.
- [vDSP_destroy_fftsetupD](vdsp_destroy_fftsetupd.md)
  Deallocates an existing double-precision FFT setup structure.
- [vDSP_DFT_CreateSetup](vdsp_dft_createsetup.md)
- [typealias FFTSetup](fftsetup.md)
  An opaque type that contains setup information for a single-precision FFT transform.
- [typealias FFTSetupD](fftsetupd.md)
  An opaque type that contains setup information for a double-precision FFT transform.
- [typealias FFTRadix](fftradix.md)
  The radix of the FFT decomposition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_create_fftsetupd)*