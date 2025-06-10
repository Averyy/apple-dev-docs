# vDSP_normalize

**Framework**: Accelerate  
**Kind**: func

Computes single-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_normalize(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Stride __IC, float * __Mean, float * __StandardDeviation, vDSP_Length __N);
```

#### Discussion

The function calculates values for `Mean` and `StandardDeviation`, then calculates new values for `A` to have a zero mean and unit standard deviation.

For iOS 9.0 and later or macOS 10.11 and later, the production of new elements may be omitted by passing `NULL` for `C`. In this case `A` remains unchanged.

## Parameters

- `__A`: Single-precision input vector.
- `__IA`: Stride for  .
- `__C`: Single-precision output vector, or   (see Discussion below).
- `__IC`: Stride for  .
- `__Mean`: Single-precision mean of the elements of  .
- `__StandardDeviation`: Single-precision standard deviation of the elements of  .
- `__N`: Number of elements in  .

## See Also

- [vDSP_normalizeD](vdsp_normalized.md)
  Computes double-precision mean and standard deviation, and then calculates new elements to have a zero mean and a unit standard deviation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_normalize)*