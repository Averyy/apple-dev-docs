# vDSP_DFT_ExecuteD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the discrete double-precision Fourier transform for a vector.

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
void vDSP_DFT_ExecuteD(const struct vDSP_DFT_SetupStructD *__Setup, const double *__Ir, const double *__Ii, double *__Or, double *__Oi);
```

#### Discussion

This function uses the following operation for a real transform. That is, when the [`vDSP_DFT_zrop_CreateSetupD`](./vdsp_dft_zrop_createsetupd.md) function provides the setup structure:

```c
// _N_ is the length given in the setup
// _h_ is the array of numbers specified by _Ir_ and _Ii_
// _H_ is the array of numbers specified by _Or_ and _Oi_
// _C_ is:
//     2 if Direction is `vDSP_DFT_FORWARD` and
//     1 if Direction is `vDSP_DFT_INVERSE`
// _S_ is:
//    -1 if Direction is `vDSP_DFT_FORWARD` and
//    +1 if Direction is `vDSP_DFT_INVERSE`
// _1**x_ is _e**(2*pi*i*x)_

For 0 <= k < N
    H[k] = C * sum(1**(S * j*k/N) * h[j], 0 <= j < N)
```

The function uses the following operation for a complex transform. That is, when the [`vDSP_DFT_zop_CreateSetupD`](./vdsp_dft_zop_createsetupd.md) function provides the setup structure:

```c
// _N_ is the length given in the setup
// _h_ is the array of complex numbers specified by _Ir_ and _Ii_
// _H_ is the array of complex numbers specified by _Or_ and _Oi_
// _S_ is:
//     -1 if Direction is `vDSP_DFT_FORWARD` and
//     +1 if Direction is `vDSP_DFT_INVERSE`
// _1**x_ is _e**(2*pi*i*x)_

For 0 <= k < N,
    H[k] = sum(1**(S * j*k/N) * h[j], 0 <= j < N),
```

This function supports in-place operation where the `Or` and `Ir` parameters are equal, and the `Oi` and `Ii` parameters are equal. The transform length must equal the transform length specified in the given setup structure.

> ❗ **Important**:  For best performance, make sure the four vector addresses passed to this function are 16-byte-aligned.

## Parameters

- `__Setup`: The DFT setup structure for this transform.
- `__Ir`: A double-precision vector that contains the real parts of the input values.
- `__Ii`: A double-precision vector that contains the imaginary parts of the input values.
- `__Or`: A double-precision vector that contains the real parts of the output values.
- `__Oi`: A double-precision vector that contains the imaginary parts of the output values.

## See Also

### Functions to perform discrete Fourier transforms
- [vDSP_DFT_Execute](./vdsp_dft_execute.md)
  Calculates the discrete single-precision Fourier transform for a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dft_executed)*