# vDSP_svdiv

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise division of a scalar value and a vector, using the specified stride.

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
extern void vDSP_svdiv(const float * __A, const float * __B, vDSP_Stride __IB, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise division of scalar value `A` and vector `B`, and writes the result to vector `C`.

```swift
 for (n = 0; n < N; ++n)
    C[n] = A / B[n];
```

![A diagram showing the operation of this function. There are three rows. The top row represents the scalar value A with one box, and the input vector B with three boxes. The middle row represents the operation as three boxes with division signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vector. ](https://docs-assets.developer.apple.com/published/de2d14d4b3697b21f34309aea77cecc1/media-4337225%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: Double = 100
    let b: [Double] = [1, 2, 3, 4, 5]
    
    let c = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_svdivD([a],
                    b, stride,
                    buffer.baseAddress!, stride,
                    vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[100.0, 50.0, 33.33, 25.0, 20.0]".
    print(c)
```

## Parameters

- `__A`: The input scalar,  .
- `__B`: The input vector,  .
- `__IB`: The distance between the elements in the input vector.
- `__C`: The output vector,  .
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_svdivD](vdsp_svdivd.md)
  Calculates the double-precision element-wise division of a scalar value and a vector, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_svdiv)*