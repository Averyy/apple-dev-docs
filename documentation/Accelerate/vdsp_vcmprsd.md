# vDSP_vcmprsD

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Generates a compressed copy of the specified double-precision vector using the nonzero values in a gating vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_vcmprsD(const double *__A, vDSP_Stride __IA, const double *__B, vDSP_Stride __IB, double *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

The following code shows an example of compressing the values in `source` using the nonzero values in `gatingVector`:

**Swift**:

```swift
    let source: [Double] = [1, 2,
                            3, 4,
                            5, 6,
                            7, 8]

    let gatingVector: [Double] = [-1, 0,
                                  1, 0,
                                  0.001, 0,
                                  10, 0]
    
    let n = vDSP_Length(source.count)
    let stride = 1
    
    let resultCount = gatingVector.filter { !$0.isZero }.count
    
    let result = [Double](unsafeUninitializedCapacity: resultCount) {
        buffer, initializedCount in
        
        vDSP_vcmprsD(source, stride,
                    gatingVector, stride,
                    buffer.baseAddress!, stride,
                    n)
        
        initializedCount = resultCount
    }
    
    // Prints "[1.0, 3.0, 5.0, 7.0]".
    print(result)
```

**Objective-C**:

```objc
    double source[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    double gatingVector[8] = {-1, 0, 1, 0, 0.001, 0, 10, 0};

    vDSP_Length n = 8;
    vDSP_Stride stride = 1;

    double result[4] = {0};

    vDSP_vcmprsD(source, stride,
                 gatingVector, stride,
                 result, stride,
                 n);

    // Prints "[1, 3, 5, 7]".
    printf("[%g, %g, %g, %g]\n", result[0], result[1], result[2], result[3]);
```

## Parameters

- `__A`: The input vector that defines the source values.
- `__IA`: The distance between the elements in the source vector.` `
- `__B`: The input vector that defines the gating values.
- `__IB`: The distance between the elements in the source vector.` `
- `__C`: The output vector.
- `__IC`: The distance between the elements in the output vector.
- `__N`: The number of elements in the output vector and the number of nonzero elements in the gating vector.

## See Also

### Vector compression
- [vDSP_vcmprs](./vdsp_vcmprs.md)
  Generates a compressed copy of the specified single-precision vector using the nonzero values in a gating vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vcmprsd)*