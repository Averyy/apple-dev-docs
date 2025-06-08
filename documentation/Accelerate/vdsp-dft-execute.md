# vDSP_DFT_Execute

**Framework**: Accelerate  
**Kind**: func

Calculates the discrete single-precision Fourier transform for a vector.

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
void vDSP_DFT_Execute(const struct vDSP_DFT_SetupStruct * __Setup, const float * __Ir, const float * __Ii, float * __Or, float * __Oi);
```

## Mentions

- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)

#### Discussion

This function uses the following operation for a real transform. That is, when the [`vDSP_DFT_zrop_CreateSetup`](vdsp_dft_zrop_createsetup.md) function provides the setup structure:

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

The function uses the following operation for a complex transform. That is, when the [`vDSP_DFT_zop_CreateSetup`](vdsp_dft_zop_createsetup.md) function provides the setup structure:

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

- [vDSP_DFT_ExecuteD](vdsp_dft_executed.md)
  Calculates the discrete double-precision Fourier transform for a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_execute)*