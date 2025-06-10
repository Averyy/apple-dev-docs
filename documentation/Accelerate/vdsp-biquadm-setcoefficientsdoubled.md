# vDSP_biquadm_SetCoefficientsDoubleD

**Framework**: Accelerate  
**Kind**: func

Sets the double-precision coefficients of the specified double-precision, multichannel biquadratic filter setup object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
extern void vDSP_biquadm_SetCoefficientsDoubleD(vDSP_biquadm_SetupD __setup, const double * __coeffs, vDSP_Length __start_sec, vDSP_Length __start_chn, vDSP_Length __nsec, vDSP_Length __nchn);
```

#### Discussion

Use this function to update sections of coefficient values of a biquadratic setup structure. This function doesn’t allocate new memory. The range that you specify using `__start_sec` and `__nsec` must be within the number of sections that you define in the create setup function.

## Parameters

- `__setup`: The biquadratic filter setup object that the function updates.
- `__coeffs`: A pointer to the new coefficients.
- `__start_sec`: The first section that the function updates.
- `__start_chn`: The first channel that the function updates.
- `__nsec`: The number of sections that the function updates.
- `__nchn`: The number of channels that the function updates.

## See Also

- [vDSP_biquadm_SetCoefficientsSingle](vdsp_biquadm_setcoefficientssingle.md)
  Sets the single-precision coefficients of the specified single-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetCoefficientsDouble](vdsp_biquadm_setcoefficientsdouble.md)
  Sets the double-precision coefficients of the specified single-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetCoefficientsSingleD](vdsp_biquadm_setcoefficientssingled.md)
  Sets the single-precision coefficients of the specified double-precision, multichannel biquadratic filter setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_setcoefficientsdoubled)*