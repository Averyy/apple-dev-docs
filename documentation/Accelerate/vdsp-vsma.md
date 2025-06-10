# vDSP_vsma

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a vector, using the specified stride.

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
extern void vDSP_vsma(const float * __A, vDSP_Stride __IA, const float * __B, const float * __C, vDSP_Stride __IC, float * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise product of vector `A` and scalar value `B`, adds vector `C` to the product, and writes the result to vector `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B + C[n];
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vector, A, with three boxes, and the scalar value B, with one box. The second row represents the operation that multiplies A and B, with three boxes, as well as the input vector C with three boxes. The third row represents the addition operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://docs-assets.developer.apple.com/published/8acd6489f7a40f9981697d673e124e2d/media-4387632%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: Float = 10
    let c: [Float] = [ 5,  4,  3,  2,  1]
    
    let d = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsma(a, stride,
                  [b],
                  c, stride,
                  buffer.baseAddress!, stride,
                  vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[15.0, 24.0, 33.0, 42.0, 51.0]".
    print(d)
```

## Parameters

- `__A`: The input vector   in  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input scalar value   in  .
- `__C`: The input vector   in  .
- `__IC`: The distance between the elements in the input vector  .
- `__D`: The output vector   in  .
- `__ID`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vsmaD](vdsp_vsmad.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a vector, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsma)*