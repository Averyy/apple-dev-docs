# vDSP_DCT_CreateSetup

**Framework**: Accelerate  
**Kind**: func

Builds a data structure that contains precalculated data to perform a discrete cosine transform.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
vDSP_DFT_Setup vDSP_DCT_CreateSetup(vDSP_DFT_Setup __Previous, vDSP_Length __Length, vDSP_DCT_Type __Type);
```

#### Return Value

When successful, this function returns a [`vDSP_DFT_Setup`](vdsp_dft_setup.md) structure. When unsuccessful, this function returns `nil`, either because of insufficient memory or because `Length` doesn’t satisfy the requirements given above.

#### Discussion

> ❗ **Important**:  To prevent potential memory leaks, if the `Previous` parameter is not `nil`, the return value and the `Previous` value must be different variables.

#### Discussion

Use this function to create a new setup structure. Don’t use the return value to reconfigure an existing setup structure passed to this function as the `Previous` parameter.

The following code creates two setup structures that share the same memory. Note that you must call [`vDSP_DFT_DestroySetup`](vdsp_dft_destroysetup.md) for both setup structures. Destroying a setup with shared data is safe; the destroy function only releases memory that’s not needed by other undestroyed setups.

```swift
var signal = [ ... ]

guard
    // Create the first setup object.
    let setupForward = vDSP_DCT_CreateSetup(nil,
                                            vDSP_Length(signal.count),
                                            .II),
    // Create the second setup object that shares resources with `setupForward`.
    let setupInverse = vDSP_DCT_CreateSetup(setupForward,
                                            vDSP_Length(signal.count),
                                            .III) else {
    NSLog("Failed to create `vDSP_DCT_CreateSetup` setup structures.")
    return
}

// Perform DCT-II transform.
vDSP_DCT_Execute(setupForward,
                 signal,
                 &signal)

// `signal` contains frequency-domain representation of the original signal.

// Perform DCT-III transform.
vDSP_DCT_Execute(setupInverse,
                 signal,
                 &signal)

// `signal` contains time-domain representation of the original signal.

// Call `vDSP_DFT_DestroySetup` on both setup structures.
vDSP_DFT_DestroySetup(setupForward)
vDSP_DFT_DestroySetup(setupInverse)
```

You should only use the returned setup structure with [`vDSP_DCT_Execute`](vdsp_dct_execute.md) using an input vector that contains `Length` elements.

## Parameters

- `__Previous`: An existing   structure that shares memory with the returned setup structure. Pass   to create an object with newly initialized and allocated memory.
- `__Length`: The number of real elements to transform. The supported values are   =   * 2** , where   is 1, 3, 5, or 15 and   is at least 4.
- `__Type`: A constant that defines which discrete cosine transform (DCT) variant to perform.

## See Also

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [enum vDSP_DCT_Type](vdsp_dct_type.md)
  Constants that indicate the type for a discrete cosine transform.
- [vDSP_DCT_Execute](vdsp_dct_execute.md)
  Calculates the discrete cosine transform for a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dct_createsetup)*