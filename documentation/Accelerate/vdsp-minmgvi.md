# vDSP_minmgvi

**Framework**: Accelerate  
**Kind**: func

Calculates the minimum magnitude and corresponding index in a single-precision vector.

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
extern void vDSP_minmgvi(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Length * __I, vDSP_Length __N);
```

#### Discussion

This function calculates the minimum magnitude and its corresponding index of the first `N` elements of the input vector and writes the results to the output scalar parameters, `C` and `I`, respectively.

![A diagram showing the operation of this function. There are three rows. The top row represents the input vector, A, with three boxes. The middle row represents the operation as two boxes that contains absolute-minimum and argmin functions. The bottom row represents the output scalar values C and I as two  boxes. The diagram has connecting lines from the input vector to the operations, and from the operations to the output scalar values.](https://docs-assets.developer.apple.com/published/3d4b3fdb64449b672c440391e857abef/media-4465981%402x.png)

The following code shows an example of using this function:

```swift
let stride = vDSP_Stride(1)

let a: [Float] = [-1.5, 2.25, 3.6,
                  0.2, -0.1, -4.3]
let n = vDSP_Length(a.count)

var c: Float = .nan
var i: vDSP_Length = 0

vDSP_minmgvi(a,
             stride,
             &c,
             &i,
             n)

// Prints "min magnitude 0.1 index 4".
print("min magnitude", c,
      "index", i) 
```

## Parameters

- `__A`: The input vector,  .
- `__IA`: The distance between the elements in the input vector.
- `__C`: The output scalar value,  . If   is zero, the function sets   to  .
- `__I`: The output scalar value,  . If   is zero, the function sets   to  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_minvi](vdsp_minvi.md)
  Calculates the minimum value and corresponding index in a single-precision vector.
- [vDSP_minviD](vdsp_minvid.md)
  Calculates the minimum value and corresponding index in a double-precision vector.
- [vDSP_minmgviD](vdsp_minmgvid.md)
  Calculates the minimum magnitude and corresponding index in a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_minmgvi)*