# vDSP_minmgvD

**Framework**: Accelerate  
**Kind**: func

Calculates the double-precision minimum magnitude of a vector.

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
extern void vDSP_minmgvD(const double * __A, vDSP_Stride __IA, double * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the minimum magnitude of the first `N` elements of input vector `A`, and writes the result to output scalar `C`.

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector, A, with three boxes. The middle row represents the operation a box that contains the absolute-minimum function. The bottom row represents the output scalar value C as a  box. The diagram has connecting lines from the input vector to the operation, and from the operation to the output scalar value.](https://docs-assets.developer.apple.com/published/c7c58a2dedd6d2361c0b00a0c4f9afd3/media-4465963%402x.png)

The following code shows an example of using this function:

```swift
    let stride = vDSP_Stride(1)

    let a: [Double] = [-1.5, 2.25, 3.6,
                      0.2, -0.1, -4.3]
    let n = vDSP_Length(a.count)

    var c = Double()

    vDSP_minmgvD(a,
                stride,
                &c,
                n)

    print("min magnitude", c) // Prints "min magnitude 0.1".
```

## Parameters

- `__A`: The input vector,  .
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output scalar value,  . If   is zero, the function sets   to  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_minv](vdsp_minv.md)
  Calculates the single-precision minimum value of a vector.
- [vDSP_minvD](vdsp_minvd.md)
  Calculates the double-precision minimum value of a vector.
- [vDSP_minmgv](vdsp_minmgv.md)
  Calculates the single-precision minimum magnitude of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_minmgvd)*