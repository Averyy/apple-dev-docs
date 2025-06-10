# vDSP_vsubD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision element-wise subtraction of two vectors, using the specified stride.

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
extern void vDSP_vsubD(const double * __B, vDSP_Stride __IB, const double * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the differences of the first `N` elements of input vectors `A` and `B`, and writes the result to output vector `C`.

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] - B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vectors, A and B, with three boxes of each. The middle row represents the operation as three boxes with minus signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vectors.](https://docs-assets.developer.apple.com/published/b6392409a61e2886a212bf90df89b30c/media-4336897%402x.png)

The following code shows an example of using this function:

```swift
let stride = 1
let count = 5

let a: [Double] = [10, 20, 30, 40, 50]
let b: [Double] = [ 1,  2,  3,  4,  5]

let c = [Double](unsafeUninitializedCapacity: count) {
    buffer, initializedCount in
    
    vDSP_vsubD(b, stride,
               a, stride,
               buffer.baseAddress!, stride,
               vDSP_Length(count))
    
    initializedCount = count
}

// Prints "[9.0, 18.0, 27.0, 36.0, 45.0]".
print(c)
```

## Parameters

- `__B`: The first input vector,  .
- `__IB`: The distance between the elements in the first input vector.
- `__A`: The second input vector,  .
- `__IA`: The distance between the elements in the second input vector.
- `__C`: The output vector,  .
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vsub](vdsp_vsub.md)
  Calculates the single-precision element-wise subtraction of two vectors, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsubd)*