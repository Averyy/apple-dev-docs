# vDSP_vthres

**Framework**: Accelerate  
**Kind**: func

Calculates single-precision vector threshold with zero fill to the specified range.

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
extern void vDSP_vthres(const float * __A, vDSP_Stride __IA, const float * __B, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

Performs the following operation:

```objc
for (n = 0; n < N; ++n){
    if (A[n*IA] >= *B)
        C[n*IC] = A[n*IA];
    else
        C[n*IC] = 0;
}
```

Creates vector `C` by comparing each input from vector `A` with scalar `*B`. If  an input value is less than `*B`, zero is written to `C`; otherwise, the input value from `A` is  copied to `C`.

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for 
- `__B`: Pointer to single-precision real input scalar: lower threshold
- `__C`: Single-precision real output vector
- `__IC`: Stride for 
- `__N`: The number of elements to process

## See Also

- [vDSP_vthresD](vdsp_vthresd.md)
  Calculates double-precision vector threshold with zero fill to the specified range.
- [vDSP_vthrsc](vdsp_vthrsc.md)
  Calculates single-precision vector threshold with signed constant to the specified range.
- [vDSP_vthrscD](vdsp_vthrscd.md)
  Calculates double-precision vector threshold with signed constant to the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vthres)*