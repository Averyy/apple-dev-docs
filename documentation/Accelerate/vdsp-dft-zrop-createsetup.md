# vDSP_DFT_zrop_CreateSetup

**Framework**: Accelerate  
**Kind**: func

Returns a setup structure that contains precalculated data for forward and inverse, real, single-precision DFT functions.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
vDSP_DFT_Setup vDSP_DFT_zrop_CreateSetup(vDSP_DFT_Setup __Previous, vDSP_Length __Length, vDSP_DFT_Direction __Direction);
```

## Mentions

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)

#### Return Value

Returns a `vDSP_DFT_Setup` object, or `nil` if the function fails, either from insufficient memory or because `Length` doesn’t satisfy the requirements given above.

#### Discussion

> ❗ **Important**:  To prevent potential memory leaks, if the `Previous` parameter is not `nil`, the return value and the `Previous` value must be different variables.

#### Discussion

This function shares memory between data structures where possible. If you have an existing setup object, you should pass that object as `Previous`. By doing so, the returned setup object can share underlying data storage with that object. Note that this function may allocate memory; you can free any allocated memory by calling [`vDSP_DFT_DestroySetup`](vdsp_dft_destroysetup.md).

##### Using Shared Setup Objects

If you’re using a shared setup object, the subsequent execute function requires that the input and output pointers are 64-byte aligned.

The following code shows how to create the correctly aligned vectors:

```swift
float* reals = (float*)aligned_alloc(64, length*sizeof(float));
float* imaginaries = (float*)aligned_alloc(64, length*sizeof(float));
```

## Parameters

- `__Previous`: An existing   structure that shares memory with the returned setup structure. Pass   to create an object with newly initialized and allocated memory.
- `__Length`: The number of real elements to process. The supported values are   * 2** , where   is 1, 3, 5, or 15 and   is at least 4.
- `__Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.

## See Also

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [vDSP_DFT_zrop_CreateSetupD](vdsp_dft_zrop_createsetupd.md)
  Returns a setup structure that contains precalculated data for forward and inverse, real, double-precision DFT functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_zrop_createsetup)*