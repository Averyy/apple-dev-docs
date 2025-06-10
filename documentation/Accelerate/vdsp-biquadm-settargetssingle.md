# vDSP_biquadm_SetTargetsSingle

**Framework**: Accelerate  
**Kind**: func

Sets the single-precision coefficient target values of the specified single-precision, multichannel biquadratic filter setup object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_biquadm_SetTargetsSingle(vDSP_biquadm_Setup __setup, const float * __targets, float __interp_rate, float __interp_threshold, vDSP_Length __start_sec, vDSP_Length __start_chn, vDSP_Length __nsec, vDSP_Length __nchn);
```

#### Discussion

This function sets target values for the biquadratic filter’s coefficients. Each subsequent call to [`vDSP_biquadm`](https://developer.apple.com/documentation/kernel/1579994-vdsp_biquadm) increments the coefficients until the difference between their values and their corresponding target is less than a specified threshold.

The size of the increment for each selected coefficient is a function of the `__interp_rate` constant and the difference between the target value and the initial value.

This function doesn’t allocate any additional memory.

The `__targets` array must only contain the new target values, and you must specify these with the same structure as the original coefficients. For more information, see [`vDSP_biquadm_CreateSetup`](vdsp_biquadm_createsetup.md).

## Parameters

- `__setup`: The biquadratic filter setup object that the function updates.
- `__targets`: The array of coefficient target values.
- `__interp_rate`: The rate constant that determines the size of increments that each call to   applies to the coefficient values. The rate must be in the range   to   otherwise, the function’s behavior is undefined.
- `__interp_threshold`: The threshold constant that determines how close a coefficient’s value must be to the target value before incrementation stops. The threshold must be greater than zero; otherwise, the function’s behavior is undefined.
- `__start_sec`: The first section in each channel that the function updates.
- `__start_chn`: The first channel that the function updates.
- `__nsec`: The number of sections in each channel that the function updates.
- `__nchn`: The number of channels that the function updates.

## See Also

- [vDSP_biquadm_SetTargetsDouble](vdsp_biquadm_settargetsdouble.md)
  Sets the double-precision coefficient target values of the specified single-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetTargetsSingleD](vdsp_biquadm_settargetssingled.md)
  Sets the single-precision coefficient target values of the specified double-precision, multichannel biquadratic filter setup object.
- [vDSP_biquadm_SetTargetsDoubleD](vdsp_biquadm_settargetsdoubled.md)
  Sets the double-precision coefficient target values of the specified double-precision, multichannel biquadratic filter setup object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_biquadm_settargetssingle)*