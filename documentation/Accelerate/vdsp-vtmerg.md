# vDSP_vtmerg

**Framework**: Accelerate  
**Kind**: func

Performs a tapered merge between two single-precision vectors.

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
extern void vDSP_vtmerg(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code performs a tapered merge between two vectors that represent sine waves at different frequencies:

```swift
    let count = 1024
    
    let vectorA: [Float] = (0 ..< count).map {
        return sin(Float($0) * 0.4)
    }
    
    let vectorB: [Float] = (0 ..< count).map {
        return sin(Float($0) * 0.025)
    }
    
    let stride = 1
    let n = vDSP_Length(count)
    
    let tapered = [Float](unsafeUninitializedCapacity: count) {
        buffer, initializedCount in
        
        vDSP_vtmerg(vectorA, stride,
                    vectorB, stride,
                    buffer.baseAddress!, stride,
                    n)
        
        initializedCount = count
    }
```

The following image shows the result of the tapered merge in `tapered`.

![Graphic showing the tapered merge from a high-frequency sine wave to a low-frequency sine wave.](https://docs-assets.developer.apple.com/published/8f7231a827070d459218346b0ddbcfc7/media-4329456%402x.png)

## Parameters

- `__A`: The first input vector.
- `__IA`: The distance between the elements in the first input vector.``
- `__B`: The second input vector.
- `__IB`: The distance between the elements in the second input vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of complex elements in the output vector.

## See Also

- [vDSP_vtmergD](vdsp_vtmergd.md)
  Performs a tapered merge between two double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vtmerg)*