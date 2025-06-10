# vDSP_vavlin

**Framework**: Accelerate  
**Kind**: func

Recalculates the element-wise single-precision linear average of an existing vector to include a second vector.

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
extern void vDSP_vavlin(const float * __A, vDSP_Stride __IA, const float * __B, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function recalculates the single-precision linear average of an existing vector to include a second vectors, using the following operation:

```swift
for (n = 0; n < N; ++n)
    C[n] = (C[n]*B[0] + A[n]) / (B[0] + 1);
```

For example, the following code calculates the average of vector `c` four times (specified by the constant `b`) plus vector `a`:

```swift
    let stride = 1
    
    let a: [Float] = [500, 2000]
    let b = Float(4)
    var c: [Float] = [250, 1000]
    
    vDSP_vavlin(
        a, stride,
        [ b ],
        &c, stride,
        vDSP_Length(c.count))
    
    // Prints "[300.0, 1200.0]":
    //     [( 250 * 4 + 500) / ( 4 + 1),
    //      (1000 * 4 + 2000) / (4 + 1)]
    print(c)
```

## Parameters

- `__A`: The input vector  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The scalar value   that defines how many times the operation multiplies the input-output vector  .
- `__C`: The input-output vector  .
- `__IC`: The distance between the elements in the input-output vector  .
- `__N`: The number of elements to process.

## See Also

- [vDSP_vavlinD](vdsp_vavlind.md)
  Recalculates the element-wise double-precision linear average of an existing vector to include a second vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vavlin)*