# vDSP_vclipcD

**Framework**: Accelerate  
**Kind**: func

Calculates and counts the elements of a double-precision vector clipped to the specified range.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vclipcD(const double * __A, vDSP_Stride __IA, const double * __B, const double * __C, double * __D, vDSP_Stride __ID, vDSP_Length __N, vDSP_Length * __NLow, vDSP_Length * __NHigh);
```

#### Discussion

This function performs the operation below:

```objc
for (n = 0; n < N; ++n) {
    if (A[n*IA] < *B)
        D[n*ID] = *B;
    else if (A[n*IA] > *C)
        D[n*ID] = *C;
    else
        D[n*ID] = A[n*IA];
}
```

On return, the output contains the clipped elements of the input. The function sets elements that are less than the low-clipping threshold to `__B`, and sets elements that are greater than the high-clipping threshold to `__C`.

The function writes the number of elements clipped to the low- and high-clipping thresholds to `__NLow` and `__NHigh`, respectively.

## Parameters

- `__A`: The input vector.
- `__IA`: The stride for the input vector.
- `__B`: A pointer to the scalar low-clipping threshold. If the low-clipping threshold is greater than the high-clipping threshold, the function calculates an undefined result.
- `__C`: A pointer to the scalar high-clipping threshold. If the high-clipping threshold is less than the low-clipping threshold, the function calculates an undefined result.
- `__D`: The output vector.
- `__ID`: The stride for the output vector.
- `__N`: The number of elements that the function clips to the specified range.
- `__NLow`: On output, the number of elements clipped to the low-clipping threshold.
- `__NHigh`: On output, the number of elements clipped to the high-clipping threshold.

## See Also

- [vDSP_vclip](vdsp_vclip.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipD](vdsp_vclipd.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [vDSP_vclipc](vdsp_vclipc.md)
  Calculates and counts the elements of a single-precision vector clipped to the specified range.
- [vDSP_viclip](vdsp_viclip.md)
  Calculates the elements of a single-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_viclipD](vdsp_viclipd.md)
  Calculates the elements of a double-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_vthr](vdsp_vthr.md)
  Calculates single-precision vector threshold to the specified range.
- [vDSP_vthrD](vdsp_vthrd.md)
  Calculates double-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vclipcd)*