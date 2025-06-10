# vDSP_vdbconD

**Framework**: Accelerate  
**Kind**: func

Converts single-precision power or amplitude values to decibel values.

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
extern void vDSP_vdbconD(const double * __A, vDSP_Stride __IA, const double * __B, double * __C, vDSP_Stride __IC, vDSP_Length __N, unsigned int __F);
```

#### Discussion

The function uses the following calculation to perform the conversion:

```swift
If Flag is 1:
    alpha = 20;
If Flag is 0:
    alpha = 10;

for (n = 0; n < N; ++n)
    C[n] = alpha * log10(A[n] / B[0]);
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__B`: The zero reference that the function uses for the conversion.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.
- `__F`: A value that specifies whether the function converts from power values or amplitude values. Set to   to specify power or   to specify amplitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vdbcond)*