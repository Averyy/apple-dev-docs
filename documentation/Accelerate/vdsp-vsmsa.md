# vDSP_vsmsa

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision element-wise addition of the product of a vector and a scalar value, and a scalar value, using the specified stride.

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
extern void vDSP_vsmsa(const float * __A, vDSP_Stride __IA, const float * __B, const float * __C, float * __D, vDSP_Stride __ID, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise product of vector `A` and scalar value `B`, adds scalar value `C` to the product, and writes the result to vector `D`.

```swift
 for (n = 0; n < N; ++n)
    D[n] = A[n] * B + C;
```

![A diagram showing the operation of this function. There are four rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The second row represents the operation that multiplies A and B, with three boxes, as well as the input vector C with three boxes. The third row represents the addition operation as three boxes. The bottom row represents the output vector D as three boxes. The diagram has connecting lines from the input vectors to the operations, and from the operations to the output vector.  ](https://docs-assets.developer.apple.com/published/13938f885dd23b946104d2e77ffe3965/media-4387657%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Float] = [ 1,  2,  3,  4,  5]
    let b: Float = 10
    let c: Float = 5
    
    let d = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsmsa(a, stride,
                   [b],
                   [c],
                   buffer.baseAddress!, stride,
                   vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[15.0, 25.0, 35.0, 45.0, 55.0]".
    print(d)
```

## Parameters

- `__A`: The input vector   in  .
- `__IA`: The distance between the elements in the input vector  .
- `__B`: The input scalar value   in  .
- `__C`: The input scalar value   in  .
- `__D`: The output vector   in  .
- `__ID`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vsmsaD](vdsp_vsmsad.md)
  Calculates the double-precision element-wise addition of the product of a vector and a scalar value, and a scalar value, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsmsa)*