# vDSP_vmmaD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision element-wise sum of the products of two pairs of vectors, using the specified stride.

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
extern void vDSP_vmmaD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, const double * __C, vDSP_Stride __IC, const double * __D, vDSP_Stride __ID, double * __E, vDSP_Stride __IE, vDSP_Length __N);
```

#### Discussion

This function calculates the differences of the first `N` elements of the product of vectors `A` and `B` and the product of vectors `C` and `D`.

```swift
 for (n = 0; n < N; ++n)
    E[n] = A[n]*B[n] + C[n]*D[n]; 
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vectors, A, B, C, and D, with three boxes of each. The second row represents the operations that multiply vectors A and B, and multiply vectors C and D, with three boxes of each. The third row represents the addition operation as three boxes.  The bottom row represents the output vector E as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vectors. ](https://docs-assets.developer.apple.com/published/ab70af179a848e3cf65eead1200fd78d/media-4470528%402x.png)

The following code shows an example of using this function:

```swift
let stride = 1
let count = 5

let a: [Double] = [ 1,  2,  3,  4,  5]
let b: [Double] = [10, 20, 30, 40, 50]
let c: [Double] = [ 5,  4,  3,  2,  1]
let d: [Double] = [50, 40, 30, 20, 10]

let e = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vmmaD(a, stride,
               b, stride,
               c, stride,
               d, stride,
               buffer.baseAddress!, stride,
               vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[260.0, 200.0, 180.0, 200.0, 260.0]".
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

- [vDSP_vmma](vdsp_vmma.md)
  Calculates the single-precision element-wise sum of the products of two pairs of vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vmmad)*