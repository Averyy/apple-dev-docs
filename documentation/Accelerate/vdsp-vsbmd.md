# vDSP_vsbmD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision element-wise product of a vector and the differences of two vectors, using the specified stride.

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
extern void vDSP_vsbmD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, const double * __C, vDSP_Stride __IC, double * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the differences of the first `N` elements of `A` and `B`, multiplies each difference by the corresponding value in `C`, and writes the result to `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = (A[n] - B[n]) * C[n];
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A and B, with three boxes of each. The second row represents the operation that subtracts B from A, as well as the input vector C, with three boxes of each. The third row represents the multiplication operation as three boxes.  The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors.  ](https://docs-assets.developer.apple.com/published/7a0b0b6f6a09540df83d4c2453dbff21/media-4337006%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Double] = [ 1,  2,  3,  4,  5]
    let b: [Double] = [10, 20, 30, 40, 50]
    let c: [Double] = [ 5,  4,  3,  2,  1]
    
    let d = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsbmD(a, stride,
                   b, stride,
                   c, stride,
                   buffer.baseAddress!, stride,
                   vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[-45.0, -72.0, -81.0, -72.0, -45.0]".
    print(d)

```

## Parameters

- `__A`: The input vector   in  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input vector   in  .
- `__IB`: The distance between the elements in the input vector  .
- `__C`: The input vector   in  .
- `__IC`: The distance between the elements in the input vector  .
- `__D`: The output vector   in  .
- `__ID`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vsbm](vdsp_vsbm.md)
  Calculates the single-precision element-wise product of a vector and the differences of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsbmd)*