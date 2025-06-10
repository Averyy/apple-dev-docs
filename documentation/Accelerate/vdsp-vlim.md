# vDSP_vlim

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision vector test limit using the specified stride.

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
extern void vDSP_vlim(const float * __A, vDSP_Stride __IA, const float * __B, const float * __C, float * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

Compares values from vector `A` to limit scalar `*B`. For inputs greater than or equal to `*B`, scalar `*C` is written to `D` . For inputs  less than `*B`, the negated value of scalar `*C` is written to vector  `D`.

This calculates the following:

```objc
    for (n = 0; n < N; ++n)
        if (*B <= A[n*IA])
            D[n*ID] = *C;
        else
            D[n*ID] = -(*C);
```

## Parameters

- `__A`: Single-precision real input vector
- `__IA`: Stride for 
- `__B`: Pointer to single-precision real input scalar: limit
- `__C`: Pointer to single-precision real input scalar
- `__D`: Single-precision real output vector
- `__ID`: Stride for 
- `__N`: The number of elements to process

## See Also

- [vDSP_vlimD](vdsp_vlimd.md)
  Calculates the double-precision vector test limit using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vlim)*