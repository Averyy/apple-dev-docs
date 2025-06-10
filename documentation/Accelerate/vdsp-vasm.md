# vDSP_vasm

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise product of the sum of two vectors and a scalar value, using the specified stride.

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
extern void vDSP_vasm(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const float * __C, float * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise sum of vectors `A` and `B`, multiplies the sum by scalar value `C`, and writes the result to vector `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = (A[n] + B[n]) * C;
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row represents the operation that adds A to B, with three boxes, as well as the input scalar C with one box. The third row represents the multiplication operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://docs-assets.developer.apple.com/published/ee957eb9f1571fd55686310874606d42/media-4383309%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: [Float] = [10, 20, 30, 40, 50]
    let c: Float = 5
    
    let d = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vasm(a, stride,
                   b, stride,
                   [c],
                   buffer.baseAddress!, stride,
                   vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[55.0, 110.0, 165.0, 220.0, 275.0]".
    print(d)
```

## Parameters

- `__A`: The input vector   in  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input vector   in  .
- `__IB`: The distance between the elements in the input vector  .
- `__C`: The input scalar value   in  .
- `__D`: The output vector   in  .
- `__ID`: The distance between the elements in the input vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vasmD](vdsp_vasmd.md)
  Calculates the double-precision element-wise product of the sum of two vectors and a scalar value, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vasm)*