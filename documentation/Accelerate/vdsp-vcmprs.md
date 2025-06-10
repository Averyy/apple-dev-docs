# vDSP_vcmprs

**Framework**: Accelerate  
**Kind**: func

Generates a compressed copy of the specified single-precision vector using the nonzero values in a gating vector.

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
extern void vDSP_vcmprs(const float * __A, vDSP_Stride __IA, const float * __B, vDSP_Stride __IB, float * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code shows an example of compressing the values in `source` using the nonzero values in `gatingVector`:

```swift
    let source: [Float] = [1, 2,
                            3, 4,
                            5, 6,
                            7, 8]

    let gatingVector: [Float] = [-1, 0,
                                  1, 0,
                                  0.001, 0,
                                  10, 0]
    
    let n = vDSP_Length(source.count)
    let stride = 1
    
    let resultCount = gatingVector.filter { !$0.isZero }.count
    
    let result = [Float](unsafeUninitializedCapacity: resultCount) {
        buffer, initializedCount in
        
        vDSP_vcmprs(source, stride,
                    gatingVector, stride,
                    buffer.baseAddress!, stride, 
                    n)
        
        initializedCount = resultCount
    }
    
    // Prints "[1.0, 3.0, 5.0, 7.0]".
    print(result)
```

## Parameters

- `__A`: The input vector that defines the source values.
- `__IA`: The distance between the elements in the source vector.
- `__B`: The input vector that defines the gating values.
- `__IB`: The distance between the elements in the source vector.
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements in the output vector and the number of nonzero elements in the gating vector.

## See Also

- [vDSP_vcmprsD](vdsp_vcmprsd.md)
  Generates a compressed copy of the specified double-precision vector using the nonzero values in a gating vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vcmprs)*