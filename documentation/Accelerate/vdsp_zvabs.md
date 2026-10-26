# vDSP_zvabs

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Calculates the absolute value of each element in the supplied single-precision complex vector using the specified stride.

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
extern void vDSP_zvabs(const DSPSplitComplex *__A, vDSP_Stride __IA, float *__C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function returns the square roots of the sum of the squares of the real and imaginary parts of each complex element.

For example, the following code calculates the absolute values of four complex numbers:

**Swift**:

```swift
    let stride = 1
    let n = 4
    
    let reals = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
    _ = reals.initialize(from: [ -3, -6, 5, 9 ])
    
    let imaginaries = UnsafeMutableBufferPointer<Float>.allocate(capacity: n)
    _ = imaginaries.initialize(from: [ 4, -8, -12, 12 ])
    
    var values = DSPSplitComplex(realp: reals.baseAddress!,
                                 imagp: imaginaries.baseAddress!)
    
    
    let absoluteValues = [Float](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP_zvabs(&values, stride,
                   buffer.baseAddress!, stride,
                   vDSP_Length(n))
        
        initializedCount = n
    }
    
    // Prints "[5.0, 10.0, 13.0, 15.0]".
    print(absoluteValues)
```

**Objective-C**:

```objc
float realp[4] = {-3, -6, 5, 9};
float imagp[4] = {4, -8, -12, 12};
DSPSplitComplex values = { .realp = realp, .imagp = imagp };

float result[4];
vDSP_zvabs(&values, 1, result, 1, 4);

// Prints "[5, 10, 13, 15]".
printf("[%g, %g, %g, %g]\n", result[0], result[1], result[2], result[3]);
```

## Parameters

- `__A`: The input vector `A`.
- `__IA`: The distance between the elements in the input vector `A`.
- `__C`: On output, the absolute values of the elements in the input vector.
- `__IC`: The distance between the elements in the output vector `C`.
- `__N`: The number of elements that the function processes.

## See Also

### Complex vector absolute functions
- [vDSP_zvabsD](./vdsp_zvabsd.md)
  Calculates the absolute value of each element in the supplied double-precision complex vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvabs)*