# vDSP_nzcros

**Framework**: Accelerate  
**Kind**: func

Counts and finds the zero crossings in a single-precision vector.

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
extern void vDSP_nzcros(const float * __A, vDSP_Stride __IA, vDSP_Length __B, vDSP_Length * __C, vDSP_Length * __D, vDSP_Length __N);
```

#### Discussion

This performs the following operation:

```objc
*D = *C = 0;
for(n = 1; n < N; n++)
{
    if( sign(A[n * IA]) != sign(A[(n - 1) * IA]) )
    {
        *D = *D + 1;
        if( *D == B)
        {
            *C = n * I;
            break;
        }
    }
}
```

The “function” sign(x) above has the value -1 if the sign bit of x is 1 (x is negative or -0), and +1 if the sign bit is 0 (x is positive or +0).

Scans vector `A` to locate transitions from positive to negative values  and from negative to positive values. The scan terminates when the number of  crossings specified by `B` is found, or the end of the vector is reached. The zero-based index of the last crossing is returned in `C`. `C` is the actual array index, not the pre-stride index. If the zero  crossing that `B` specifies is not found, zero is returned in `C`. The total number of  zero crossings found is returned in `D`.

Note that a transition from -0 to +0 or from +0 to -0 is counted as a zero crossing.

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Address stride for  .
- `__B`: Maximum number of crossings to find.
- `__C`: Index of last crossing found.
- `__D`: Total number of zero crossings found
- `__N`: Number of elements in  .

## See Also

- [vDSP_nzcrosD](vdsp_nzcrosd.md)
  Counts and finds the zero crossings in a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_nzcros)*