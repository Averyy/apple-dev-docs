# vDSP_vsaddD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision element-wise sum of a vector and a scalar value, using the specified stride.

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
extern void vDSP_vsaddD(const double * __A, vDSP_Stride __IA, const double * __B, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function calculates the element-wise sum of vector `A` and scalar value `B`, and writes the result to vector `C`.

```swift
 for (n = 0; n < N; ++n)
    C[n] = A[n] + B;
```

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector A with three boxes, and the scalar value B with one box. The middle row represents the operation as three boxes with plus signs. The bottom row represents the output vector C as three boxes. The diagram has connecting lines from the input vectors to the operation, and from the operation to the output vector. ](https://docs-assets.developer.apple.com/published/a002ac762dcf00ea77f65483b7339474/media-4337161%402x.png)

The following code shows an example of using this function:

```swift
    let stride = 1
    let count = 5
    
    let a: [Double] = [1, 2, 3, 4, 5]
    let b: Double = 10
    
    let c = [Double](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vsaddD(a, stride,
                    [b],
                    buffer.baseAddress!, stride,
                    vDSP_Length(count))
        
        initializedCount = count
    }
    
    // Prints "[11.0, 12.0, 13.0, 14.0, 15.0]".
    print(c)
```

## Parameters

- `__A`: The input vector,  .
- `__IA`: The distance between the elements in the input vector.
- `__B`: The input scalar,  .
- `__C`: The output vector,  .
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_vsaddi](vdsp_vsaddi.md)
  Calculates the integer element-wise sum of a vector and a scalar value, using the specified stride.
- [vDSP_vsadd](vdsp_vsadd.md)
  Calculates the single-precision element-wise sum of a vector and a scalar value, using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vsaddd)*