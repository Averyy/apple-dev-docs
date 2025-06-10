# vDSP_vasbm

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors, using the specified stride.

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
extern void vDSP_vasbm(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const float * __C, vDSP_Stride __IC, const float * __D, vDSP_Stride __ID, float * __E, vDSP_Stride __IE, vDSP_Length __N);
```

#### Discussion

This function calculates the products of the first `N` elements of the addition of vectors `A` and `B` and the subtraction of vectors `C` and `D`.

```swift
 for (n = 0; n < N; ++n)
    E[n] = (B[n]+A[n]) * (C[n]-D[n]); 
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A, B, C, and D, with three boxes of each. The second row represents the operations that add vectors A and B, and subtract vectors C and D, with three boxes of each. The third row represents the multiplication operation as three boxes.  The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.  ](https://docs-assets.developer.apple.com/published/db5da83a4f1f64eeae4531beae3c5d08/media-4337130%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: [Float] = [10, 20, 30, 40, 50]
    let c: [Float] = [ 5,  4,  3,  2,  1]
    let d: [Float] = [50, 40, 30, 20, 10]
    
    
    let e = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vasbm(a, stride,
                   b, stride,
                   c, stride,
                   d, stride,
                   buffer.baseAddress!, stride,
                   vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[-495.0, -792.0, -891.0, -792.0, -495.0]".
    print(e)

```

## Parameters

- `__A`: The input vector   in  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input vector   in  .
- `__IB`: The distance between the elements in the input vector  .
- `__C`: The input vector   in  .
- `__IC`: The distance between the elements in the input vector  .
- `__D`: The input vector   in  .
- `__ID`: The distance between the elements in the input vector  .
- `__E`: The output vector   in  .
- `__IE`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vasbmD](vdsp_vasbmd.md)
  Calculates the double-precision element-wise product of the sum of two vectors and the difference of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vasbm)*