# vDSP_vgenpD

**Framework**: Accelerate  
**Kind**: func

Generates the double-precision linearly interpolated values of a vector at the specified indices.

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
extern void vDSP_vgenpD(const double * __A, vDSP_Stride __IA, const double * __B, vDSP_Stride __IB, double * __C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __M);
```

## Mentions

- [Using linear interpolation to construct new data points](using-linear-interpolation-to-construct-new-data-points.md)

#### Discussion

The following code creates a five-element vector from two values using linear interpolation. The last index in `indices` determines the length of the operation result.

```swift
    let values: [Double] = [0, 100]
    let indices: [Double] = [0, 4]
    
    let n = Int(indices.last! + 1)
    let m = values.count
    
    let stride = 1
    
    let interpolatedValues = [Double](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP_vgenpD(values, stride,
                    indices, stride,
                    buffer.baseAddress!, stride,
                    vDSP_Length(n),
                    vDSP_Length(m))
        
        initializedCount = n
    }
    
    // Prints "[0.0, 25.0, 50.0, 75.0, 100.0]".
    print(interpolatedValues)
```

## Parameters

- `__A`: The input vector that defines the values that the function interpolates.
- `__IA`: The distance between the elements in the values vector.
- `__B`: The input vector that defines the indices at which the function interpolates.
- `__IB`: The distance between the elements in the indices vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements that the function processes.
- `__M`: The number of elements in the values and indices input vectors.

## See Also

- [vDSP_vgenp](vdsp_vgenp.md)
  Generates the single-precision linearly interpolated values of a vector at the specified indices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vgenpd)*