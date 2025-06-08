# vDSP_DFT_Interleaved_CreateSetup(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a setup structure that contains precalculated data for forward and inverse, single-precision interleaved discrete Fourier transform (DFT) functions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func vDSP_DFT_Interleaved_CreateSetup(_ Previous: vDSP_DFT_Interleaved_Setup?, _ Length: vDSP_Length, _ Direction: vDSP_DFT_Direction, _ RealtoComplex: vDSP_DFT_RealtoComplex) -> vDSP_DFT_Interleaved_Setup?
```

#### Return Value

Returns a [`vDSP_DFT_Interleaved_Setup`](vdsp_dft_interleaved_setup.md) object, or `nil` if the function fails, either from insufficient memory or because `Length` doesn’t satisfy the above requirements.

#### Discussion

> ❗ **Important**:  To prevent potential memory leaks, if the `Previous` parameter is not `nil`, the return value and the `Previous` value must be different variables.

#### Discussion

The interleaved DFT operations that the Accelerate framework provides work over collections with specific counts. The maximum number of complex elements that these operations support is 4,096, and other supported counts are the result of the formula `f * 2ⁿ` for certain values of `f` and `n`. In the case of real-to-complex, `n` is the number of real elements divided by two, and for complex-to-complex `n` is the number of complex elements.

The following tables show the complete list of supported lengths for different values of `f` and `n`.

##### Supported Lengths for F = 1

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |
| 8 | 256 |  |
| 9 | 512 |  |
| 10 | 1,024 |  |
| 11 | 2,048 |  |
| 12 | 4,096 |  |

##### Supported Lengths for F = 3

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |
| 8 | 256 |  |

##### Supported Lengths for F = 5

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |

##### Supported Lengths for F = 9

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |

##### Supported Lengths for F = 15

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |

## Parameters

- `Previous`: An existing   structure that shares memory and direction with the setup structure that this function returns. Pass   to create an object with newly initialized and allocated memory. To ensure correct operation, if you specify a previous setup structure it must share the same direction as the   parameter.
- `Length`: For real-to-complex transforms, the number of real elements divided by 2.
- `Direction`: A flag that specifies the transform direction. Pass   to transform from the time domain to the frequency domain. Pass   to transform from the frequency domain to the time domain.
- `RealtoComplex`: A flag that specifies the transform type. To transform from complex to complex, pass  . To transform from real to complex, pass  .

## See Also

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
  Format source data for the vDSP Fourier functions, and interpret the results.
- [Reducing spectral leakage with windowing](reducing-spectral-leakage-with-windowing.md)
  Multiply signal data by window sequence values when performing transforms with noninteger period signals.
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
  Optimize discrete Fourier transform (DFT) performance with the vDSP interleaved DFT routines.
- [func vDSP_DFT_Interleaved_CreateSetupD(vDSP_DFT_Interleaved_SetupD?, vDSP_Length, vDSP_DFT_Direction, vDSP_DFT_RealtoComplex) -> vDSP_DFT_Interleaved_SetupD?](vdsp_dft_interleaved_createsetupd(_:_:_:_:).md)
  Returns a setup structure that contains precalculated data for forward and inverse, double-precision interleaved discrete Fourier transform (DFT) functions.
- [func vDSP_DFT_Interleaved_Execute(vDSP_DFT_Interleaved_Setup, UnsafePointer<DSPComplex>, UnsafeMutablePointer<DSPComplex>)](vdsp_dft_interleaved_execute(_:_:_:).md)
  Calculates the single-precision discrete Fourier transform (DFT)  for a vector of interleaved complex values.
- [func vDSP_DFT_Interleaved_ExecuteD(vDSP_DFT_Interleaved_SetupD, UnsafePointer<DSPDoubleComplex>, UnsafeMutablePointer<DSPDoubleComplex>)](vdsp_dft_interleaved_executed(_:_:_:).md)
  Calculates the double-precision discrete Fourier transform (DFT) for a vector of interleaved complex values.
- [func vDSP_DFT_Interleaved_DestroySetup(vDSP_DFT_Interleaved_Setup?)](vdsp_dft_interleaved_destroysetup(_:).md)
  Releases a single-precision discrete Fourier transform (DFT) setup structure.
- [func vDSP_DFT_Interleaved_DestroySetupD(vDSP_DFT_Interleaved_SetupD?)](vdsp_dft_interleaved_destroysetupd(_:).md)
  Releases a double-precision discrete Fourier transform (DFT) setup structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_interleaved_createsetup(_:_:_:_:))*