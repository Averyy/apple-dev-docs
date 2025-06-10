# vDSP_vma

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise sum of a vector and the product of two vectors, using the specified stride.

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
extern void vDSP_vma(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const float * __C, vDSP_Stride __IC, float * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the products of the first `N` elements of `A` and `B`, adds each product to the corresponding value in `C`, and writes the result to `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = (A[n] * B[n]) + C[n];
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row represents the operation that multiplies A and B, as well as the input vector C, with three boxes of each. The third row represents the addition operation as three boxes.  The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.  ](https://docs-assets.developer.apple.com/published/ff9d5e0e42fb64a3d1e6c0c7b21a9b24/media-4336970%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: [Float] = [10, 20, 30, 40, 50]
    let c: [Float] = [ 5,  4,  3,  2,  1]
    
    let d = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vma(a, stride,
                 b, stride,
                 c, stride,
                 buffer.baseAddress!, stride,
                 vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[15.0, 44.0, 93.0, 162.0, 251.0]".
    print(d)

```

## Parameters

- `__A`: The input vector   in  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input vector   in  .
- `__IB`: The distance between the elements in the input vector  .
- `__C`: The input vector   in  .
- `__IC`: The distance between the elements in the input vector C.
- `__D`: The output vector   in  .
- `__ID`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vmaD](vdsp_vmad.md)
  Calculates the double-precision element-wise sum of a vector and the product of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vma)*