# vDSP_vsbsbm

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise product of the differences of two pairs of vectors, using the specified stride.

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
extern void vDSP_vsbsbm(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, const float * __C, vDSP_Stride __IC, const float * __D, vDSP_Stride __ID, float * __E, vDSP_Stride __IE, vDSP_Length __N);
```

#### Discussion

This function calculates the products of the first `N` elements of the subtraction of vectors `A` and `B` and the subtraction of vectors `C` and `D`.

```swift
 for (n = 0; n < N; ++n)
    E[n] = (B[n]-A[n]) * (D[n]-C[n]); 
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A, B, C, and D, with three boxes of each. The second row represents the operations that subtract vectors A and B, and subtract vectors C and D, with three boxes of each. The third row represents the multiplication operation as three boxes.  The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.  ](https://docs-assets.developer.apple.com/published/dde9ea275773abe430796095cb2213ac/media-4337092%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let b: [Float] = [10, 20, 30, 40, 50]
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let d: [Float] = [50, 40, 30, 20, 10]
    let c: [Float] = [ 5,  4,  3,  2,  1]
    
    
    let e = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsbsbm(a, stride,
                    b, stride,
                    c, stride,
                    d, stride,
                    buffer.baseAddress!, stride,
                    vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[605.0, 968.0, 1089.0, 968.0, 605.0]".
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

- [vDSP_vsbsbmD](vdsp_vsbsbmd.md)
  Calculates the double-precision element-wise product of the differences of two pairs of vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsbsbm)*