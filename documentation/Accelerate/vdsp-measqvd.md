# vDSP_measqvD

**Framework**: Accelerate  
**Kind**: func

Calculates the mean of squares of a double-precision vector.

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
extern void vDSP_measqvD(const double * __A, vDSP_Stride __I, double * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the mean of squares of the first `N` elements of the input vector and writes the result to the output scalar parameter, `C`.

The following code shows an example of using [`vDSP_measqvD`](vdsp_measqvd.md):

```swift
    let stride = vDSP_Stride(1)
    
    let a: [Double] = [-8, -4, -2, 0, 2, 4, 8]
    let n = vDSP_Length(a.count)
    
    var c = Double()
    
    vDSP_measqvD(a,
                 stride,
                 &c,
                 n)
    
    print(c) // Prints "24.0".
```

## Parameters

- `__A`: The input vector.
- `__I`: The distance between the elements in the input vector.
- `__C`: On output, the mean of squares of the elements in the input vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_measqv](vdsp_measqv.md)
  Calculates the mean of squares of a single-precision vector.
- [vDSP_mvessq](vdsp_mvessq.md)
  Calculates the mean of signed squares of a single-precision vector.
- [vDSP_mvessqD](vdsp_mvessqd.md)
  Calculates the mean of signed squares of a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_measqvd)*