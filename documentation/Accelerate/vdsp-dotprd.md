# vDSP_dotprD

**Framework**: Accelerate  
**Kind**: func

Calculates the dot product of two double-precision vectors.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_dotprD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the dot product of two vectors, using the following operation:

```objc
C[0] = sum(A[n] * B[n], 0 <= n < N);
```

For example, the following code calculates the dot product of the two vectors `[1, 2, 3]` and `[4, 5, 6]` as `(1*4)+(2*5)+(3*6)=32`:

```swift
    let stride = 1
    let n = 3
    
    let a: [Double] = [1.0, 2.0, 3.0]
    let b: [Double] = [4.0, 5.0, 6.0]
    
    var c = Double()
    
    vDSP_dotprD(a, stride,
                b, stride,
                &c,
                vDSP_Length(n))
    
    // Prints "32.0".
    print(c)
```

## Parameters

- `__A`: The input vector  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input vector  .
- `__IB`: The distance between the elements in the input vector  .
- `__C`: On output, the dot product of the two vectors.
- `__N`: The number of elements to process.

## See Also

- [vDSP_dotpr](vdsp_dotpr.md)
  Calculates the dot product of two single-precision vectors.
- [vDSP_dotpr_s1_15](vdsp_dotpr_s1_15.md)
  Calculates the dot product of two fixed-point 1.15 format vectors.
- [vDSP_dotpr_s8_24](vdsp_dotpr_s8_24.md)
  Calculates the dot product of two fixed-point  8.24 format vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_dotprd)*