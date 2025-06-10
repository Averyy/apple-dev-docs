# vDSP_vclip

**Framework**: Accelerate  
**Kind**: func

Calculates the elements of a single-precision vector clipped to the specified range.

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
extern void vDSP_vclip(const float * __A, vDSP_Stride __IA, const float * __B, const float * __C, float * __D, vDSP_Stride __ID, vDSP_Length __N);
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

## Parameters

- `__A`: The input vector.
- `__IA`: The stride for the input vector.
- `__B`: A pointer to the scalar low-clipping threshold. If the low-clipping threshold is greater than the high-clipping threshold, the function calculates an undefined result.
- `__C`: A pointer to the scalar high-clipping threshold. If the high-clipping threshold is less than the low-clipping threshold, the function calculates an undefined result.
- `__D`: The output vector.
- `__ID`: The stride for the output vector.
- `__N`: The number of elements that the function clips to the specified range.

## See Also

- [vDSP_vclipD](vdsp_vclipd.md)
  Calculates the elements of a double-precision vector clipped to the specified range.
- [vDSP_vclipc](vdsp_vclipc.md)
  Calculates and counts the elements of a single-precision vector clipped to the specified range.
- [vDSP_vclipcD](vdsp_vclipcd.md)
  Calculates and counts the elements of a double-precision vector clipped to the specified range.
- [vDSP_viclip](vdsp_viclip.md)
  Calculates the elements of a single-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_viclipD](vdsp_viclipd.md)
  Calculates the elements of a double-precision vector inverted-clipped to the specified range using the specified stride.
- [vDSP_vthr](vdsp_vthr.md)
  Calculates single-precision vector threshold to the specified range.
- [vDSP_vthrD](vdsp_vthrd.md)
  Calculates double-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vclip)*