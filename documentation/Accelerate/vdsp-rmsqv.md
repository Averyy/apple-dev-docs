# vDSP_rmsqv

**Framework**: Accelerate  
**Kind**: func

Calculates the root mean square of a single-precision vector.

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
extern void vDSP_rmsqv(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Length __N);
```

#### Discussion

This function calculates the root mean square of the first `N` elements of the input vector and writes the result to the output scalar parameter, `C`.

The following code shows an example of using [`vDSP_rmsqv`](vdsp_rmsqv.md):

```swift
    let stride = vDSP_Stride(1)
    
    let a: [Float] = [-8, -4, -2, 0, 2, 4, 8]
    let n = vDSP_Length(a.count)
    
    var c = Float()
    
    vDSP_rmsqv(a,
               stride,
               &c,
               n)
    
    print(c) // Prints "4.89".
```

## Parameters

- `__A`: The input vector.
- `__IA`: The distance between the elements in the input vector.
- `__C`: On output, the root mean square of the elements in the input vector.
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_rmsqvD](vdsp_rmsqvd.md)
  Calculates the root mean square of a double-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_rmsqv)*