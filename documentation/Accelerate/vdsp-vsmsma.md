# vDSP_vsmsma

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise addition of two vector-scalar products, using the specified stride.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vsmsma(const float * __A, vDSP_Stride __IA, const float * __B, const float * __C, vDSP_Stride __IC, const float * __D, float * __E, vDSP_Stride __IE, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise vector-scalar products of `A` and `B`, and `C` and `D`, and writes the sum of the products to vector `D`.

```swift
for (n = 0; n < N; ++n)
    E[n] = A[n]*B + C[n]*D;
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and C, with three boxes each, and the scalar values, B and D, with one box each. The second row represents the operations that multiply A and B, as well as the operations that multiply C and D, with three boxes each. The third row represents the addition operation as three boxes. The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://docs-assets.developer.apple.com/published/b6cb0eeedb42d8a2f4567d801ec83105/media-4389075%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: Float = 10
    let c: [Float] = [ 5,  4,  3,  2,  1]
    let d: Float = 50
    
    let e = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsmsma(a, stride,
                    [b],
                    c, stride,
                    [d],
                    buffer.baseAddress!, stride,
                    vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[260.0, 220.0, 180.0, 140.0, 100.0]".
    print(e)
```

## Parameters

- `__A`: The input vector   in  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input scalar value   in  .
- `__C`: The input vector   in  .
- `__IC`: The distance between the elements in the input vector  .
- `__D`: The input scalar value   in  .
- `__E`: The output vector   in  .
- `__IE`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vsmsmaD](vdsp_vsmsmad.md)
  Calculates the double-precision element-wise addition of two vector-scalar products, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsmsma)*