# vDSP_svemgD

**Framework**: Accelerate  
**Kind**: func

Calculates the sum of magnitudes in a double-precision vector.

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
extern void vDSP_svemgD(const double * __A, vDSP_Stride __IA, double * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the sum of magnitudes of the first `N` elements of `A` and writes the result to `C`:

![A diagram showing the operation of the vDSP_svemg function. There are three rows. The top row represents the input, vector A. The second row represents the summation operation. The bottom row represents the output, vector C. The diagram has connecting lines from the input vectors to the operation and from the operation to the output vector indicating the relationships between the input and output.](https://docs-assets.developer.apple.com/published/9f73e8bdb852b6ac855e783fd428fb29/media-3226728%402x.png)

The operation is:

```c
C[0] = sum(|A[n]|, 0 <= n < N);
```

## Parameters

- `__A`: Single-precision real input vector.
- `__IA`: Stride for 
- `__C`: Single-precision real output scalar
- `__N`: The number of elements to process

## See Also

- [vDSP_sve](vdsp_sve.md)
  Calculates the sum of values in a single-precision vector.
- [vDSP_sveD](vdsp_sved.md)
  Calculates the sum of values in a double-precision vector.
- [vDSP_svemg](vdsp_svemg.md)
  Calculates the sum of magnitudes in a single-precision vector.
- [vDSP_svesq](vdsp_svesq.md)
  Calculates the sum of squares in a single-precision vector.
- [vDSP_svesqD](vdsp_svesqd.md)
  Calculates the sum of squares in a double-precision vector.
- [vDSP_sve_svesq](vdsp_sve_svesq.md)
  Calculates the sum of values and the sum of squares in a single-precision vector.
- [vDSP_sve_svesqD](vdsp_sve_svesqd.md)
  Calculates the sum of values and the sum of squares in a double-precision vector.
- [vDSP_svs](vdsp_svs.md)
  Calculates the sum of signed squares in a single-precision vector.
- [vDSP_svsD](vdsp_svsd.md)
  Calculates the sum of signed squares in a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_svemgd)*