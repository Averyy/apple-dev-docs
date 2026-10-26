# vDSP_DFT_zop_CreateSetupD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a setup structure that contains precalculated data for forward and inverse, complex, double-precision DFT functions.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
vDSP_DFT_SetupDvDSP_DFT_zop_CreateSetupD(vDSP_DFT_SetupD __Previous, vDSP_Length __Length, vDSP_DFT_Direction __Direction);
```

#### Return Value

Returns a [`vDSP_DFT_SetupD`](./vdsp_dft_setupd.md) object, or `nil` if the function fails, either from insufficient memory or because `Length` doesn’t satisfy the requirements given above.

#### Discussion

> ❗ **Important**:  To prevent potential memory leaks, if the `Previous` parameter is not `nil`, the return value and the `Previous` value must be different variables.

#### Discussion

This function shares memory between data structures where possible. If you have an existing setup object, you should pass that object as `Previous`. By doing so, the returned setup object can share underlying data storage with that object. Note that this function may allocate memory; you can free any allocated memory by calling  [`vDSP_DFT_DestroySetupD`](./vdsp_dft_destroysetupd.md).

##### Using shared setup objects

If you’re using a shared setup object, the subsequent execute function requires that the input and output pointers are 64-byte aligned.

The following code shows how to create the correctly aligned vectors:

```c
double* reals = (double*)aligned_alloc(64, length*sizeof(double));
double* imaginaries = (double*)aligned_alloc(64, length*sizeof(double));
```

## Parameters

- `__Previous`: An existing [`vDSP_DFT_SetupD`](./vdsp_dft_setupd.md) structure that shares memory with the returned setup structure. Pass `nil` to create an object with newly initialized and allocated memory.
- `__Length`: The number of complex elements to process. The supported values are *f* * 2***n*, where *f* is 1, 3, 5, or 15 and *n* is at least 3.
- `__Direction`: A flag that specifies the transform direction. Pass [`vDSP_DFT_Direction.FORWARD`](./vdsp_dft_direction/forward.md) to transform from the time domain to the frequency domain. Pass [`vDSP_DFT_Direction.INVERSE`](./vdsp_dft_direction/inverse.md) to transform from the frequency domain to the time domain.

## See Also

### Related Documentation
- [Understanding data packing for Fourier transforms](./understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Reducing spectral leakage with windowing](./reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
### Complex discrete Fourier transform setup
- [vDSP_DFT_zop_CreateSetup](./vdsp_dft_zop_createsetup.md)
  Returns a setup structure that contains precalculated data for forward and inverse, complex, single-precision DFT functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_zop_createsetupd)*