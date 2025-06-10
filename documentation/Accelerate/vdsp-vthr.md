# vDSP_vthr

**Framework**: Accelerate  
**Kind**: func

Calculates single-precision vector threshold to the specified range.

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
extern void vDSP_vthr(const float * __A, vDSP_Stride __IA, const float * __B, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

```objc
for (n = 0; n < N; ++n){
    if (A[n*IA] >= *B)
        C[n*IC] = A[n*IA];
    else
        C[n*IC] = *B;
}
```

Creates vector `C` by comparing each input from vector `A` with scalar `*B`. If  an input value is less than `*B`, `*B` is copied to `C`; otherwise, the input value from `A` is  copied to `C`.

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for 
- `__B`: Pointer to single-precision real input scalar: lower threshold
- `__C`: Single-precision real output vector
- `__IC`: Stride for 
- `__N`: The number of elements to process

## See Also

- [vDSP_vclip](vdsp_vclip.md)
  Calculates the elements of a single-precision vector clipped to the specified range.
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
- [vDSP_vthrD](vdsp_vthrd.md)
  Calculates double-precision vector threshold to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthr)*