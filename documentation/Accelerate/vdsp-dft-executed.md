# vDSP_DFT_ExecuteD

**Framework**: Accelerate  
**Kind**: func

Calculates the discrete double-precision Fourier transform for a vector.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
void vDSP_DFT_ExecuteD(const struct vDSP_DFT_SetupStructD * __Setup, const double * __Ir, const double * __Ii, double * __Or, double * __Oi);
```

#### Discussion

This function uses the following operation for a real transform. That is, when the [`vDSP_DFT_zrop_CreateSetupD`](vdsp_dft_zrop_createsetupd.md) function provides the setup structure:

```swift
// `N` is the Length given in the setup
// `h` is the array of numbers specified by `Ir` and `Ii` 
// `H` is the array of numbers specified by `Or` and `Oi` 
// `C` is: 
//     2 if Direction is vDSP_DFT_FORWARD and 
//     1 if Direction is vDSP_DFT_INVERSE
// `S` is:
//    -1 if Direction is vDSP_DFT_FORWARD and 
//    +1 if Direction is vDSP_DFT_INVERSE
// `1**x` is `e**(2*pi*i*x)`

For 0 <= k < N
    H[k] = C * sum(1**(S * j*k/N) * h[j], 0 <= j < N)
```

The function uses the following operation for a complex transform. That is, when the [`vDSP_DFT_zop_CreateSetupD`](vdsp_dft_zop_createsetupd.md) function provides the setup structure:

```swift
// `N` is the length given in the setup
// `h` is the array of complex numbers specified by Ir and Ii
// `H` is the array of complex numbers specified by Or and Oi
// `S` is:
//     -1 if Direction is vDSP_DFT_FORWARD and 
//     +1 if Direction is vDSP_DFT_INVERSE
// `1**x` is `e**(2*pi*i*x)`

For 0 <= k < N,
    H[k] = sum(1**(S * j*k/N) * h[j], 0 <= j < N),
```

This function supports in-place operation where the `Or` and `Ir` parameters are equal, and the `Oi` and `Ii` parameters are equal. The transform length must equal the transform length specified in the given setup structure.

> ❗ **Important**:  For best performance, make sure the four vector addresses passed to this function are 16-byte-aligned.

## Parameters

- `__Setup`: The DFT setup structure for this transform.
- `__Ir`: A single-precision vector that contains the real parts of the input values.
- `__Ii`: A single-precision vector that contains the imaginary parts of the input values.
- `__Or`: A single-precision vector that contains the real parts of the output values.
- `__Oi`: A single-precision vector that contains the imaginary parts of the output values.

## See Also

- [vDSP_DFT_Execute](vdsp_dft_execute.md)
  Calculates the discrete single-precision Fourier transform for a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_executed)*