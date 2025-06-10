# vDSP_zvabsD

**Framework**: Accelerate  
**Kind**: func

Calculates the absolute value of each element in the supplied double-precision complex vector using the specified stride.

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
extern void vDSP_zvabsD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, double * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

This function returns the square roots of the sum of the squares of the real and imaginary parts of each complex element.

For example, the following code calculates the absolute values of four complex numbers:

```swift
    let stride = 1
    let n = 4
    
    let reals = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = reals.initialize(from: [ -3, -6, 5, 9 ])
    
    let imaginaries = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = imaginaries.initialize(from: [ 4, -8, -12, 12 ])
    
    var values = DSPDoubleSplitComplex(realp: reals.baseAddress!,
                                       imagp: imaginaries.baseAddress!)
    
    
    let absoluteValues = [Double](unsafeUninitializedCapacity: n) {
        buffer, initializedCount in
        
        vDSP_zvabsD(&values, stride,
                    buffer.baseAddress!, stride,
                    vDSP_Length(n))
        
        initializedCount = n
    }
    
    // Prints "[5.0, 10.0, 13.0, 15.0]".
    print(absoluteValues)
```

## Parameters

- `__A`: The input vector  .
- `__IA`: The distance between the elements in the input vector  .
- `__C`: On output, the absolute values of the elements in the input vector.
- `__IC`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_zvabs](vdsp_zvabs.md)
  Calculates the absolute value of each element in the supplied single-precision complex vector using the specified stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvabsd)*