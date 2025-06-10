# vDSP_biquad_SetCoefficientsSingle

**Framework**: Accelerate  
**Kind**: func

Sets single-precision coefficients of the specified single-channel biquadratic filter setup object.

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
extern void vDSP_biquad_SetCoefficientsSingle(vDSP_biquad_Setup __setup, const float * __coeffs, vDSP_Length __start_sec, vDSP_Length __nsec);
```

#### Discussion

Use this function to update sections of coefficient values of a biquad setup structure. This function doesn’t allocate new memory. The range that you specify using `__start_sec` and `__nsec` must be within the number of sections that you define in the create setup function.

## Parameters

- `__setup`: The biquadratic filter setup object that the function updates.
- `__coeffs`: A pointer to the new coefficients.
- `__start_sec`: The first section that the function updates.
- `__nsec`: The number of sections that the function updates.

## See Also

- [vDSP_biquad_SetCoefficientsDouble](vdsp_biquad_setcoefficientsdouble.md)
  Sets double-precision coefficients of the specified single-channel biquadratic filter setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquad_setcoefficientssingle)*