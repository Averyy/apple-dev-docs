# vDSP_desamp

**Framework**: Accelerate  
**Kind**: func

Performs single-precision FIR filtering with decimation and antialiasing.

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
extern void vDSP_desamp(const float * __A, vDSP_Stride __DF, const float * __F, float * __C, vDSP_Length __N, vDSP_Length __P);
```

## Mentions

- [Resampling a signal with decimation](resampling-a-signal-with-decimation.md)

#### Discussion

Performs finite impulse response (FIR) filtering at selected positions of the input vector `A`, with the filter `F`, using the decimation factor `DF`. Results are left in the output vector `C`.

This function can run in place, but `C` cannot be in place with `F`.

This function’s operation is indicated by the following pseudocode:

```objc
for (n = 0; n < N; ++n)
{
    sum = 0;
    for (p = 0; p < P; ++p)
        sum += A[n * DF + p] * F[p];
    C[n] = sum;
}
```

> **Note**:  The [`vDSP_desamp`](vdsp_desamp.md) function may rearrange the order of operations and use various floating-point precisions, so actual results may not be calculated in exactly the same way as the pseudocode above.

## Parameters

- `__A`: Single-precision real input vector. The size of   must be at least   (see below).
- `__DF`: Decimation factor.
- `__F`: Single-precision real filter vector.
- `__C`: Single-precision real output vector.
- `__N`: Length of output vector  .
- `__P`: Length of filter vector  .

## See Also

- [vDSP_desampD](vdsp_desampd.md)
  Performs double-precision FIR filtering with decimation and antialiasing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_desamp)*