# vDSP_minv

**Framework**: Accelerate  
**Kind**: func

Calculates the single-precision minimum value of a vector.

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
extern void vDSP_minv(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the minimum value of the first `N` elements of input vector `A`, and writes the result to output scalar `C`.

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector, A, with three boxes. The middle row represents the operation a box that contains the minimum function. The bottom row represents the output scalar value C as a  box. The diagram has connecting lines from the input vector to the operation, and from the operation to the output scalar value.](https://docs-assets.developer.apple.com/published/350e3d97cfe57f710e8f68eb6505edf4/media-4465973%402x.png)

The following code shows an example of using this function:

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c = Float()

vDSP_minv(a,
          stride,
          &c,
          n)

print("min", c) // Prints "min -4.3".
```

## Parameters

- `__A`: The input vector,  .
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output scalar value,  . If   is zero, the function sets   to  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_minvD](vdsp_minvd.md)
  Calculates the double-precision minimum value of a vector.
- [vDSP_minmgv](vdsp_minmgv.md)
  Calculates the single-precision minimum magnitude of a vector.
- [vDSP_minmgvD](vdsp_minmgvd.md)
  Calculates the double-precision minimum magnitude of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_minv)*