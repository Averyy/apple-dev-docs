# vDSP_deq22D

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs two-pole two-zero recursive filtering on a double-precision vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_deq22D(const double *__A, vDSP_Stride __IA, const double *__B, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Discussion

This function is the same as [`vDSP_deq22`](../kernel/api-1532225-vdsp_deq22.md), except for the types of vectors `A`, `B`, and `C`..

## See Also

### Vector-to-Vector Recursive Filtering on Real Vectors
- [vDSP_deq22](./vdsp_deq22.md)
  Performs two-pole two-zero recursive filtering on a single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_deq22d)*