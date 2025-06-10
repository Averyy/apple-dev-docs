# vDSP_zvnegD

**Framework**: Accelerate  
**Kind**: func

Calculates the negative value of each element in the supplied complex double-precision vector.

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
extern void vDSP_zvnegD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

For example, the following code calculates the negative values of the elements of an array:

```swift
    let stride = 1
    let n = 8
    
    let srcReals = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = srcReals.initialize(from: [-1, 2, -3, 4, -5, 6, -7, 8])
    
    let srcImaginaries = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    _ = srcImaginaries.initialize(from: [ 10, 20, 30, 40, -50, -60, -70, -80])
    
    var srcValues = DSPDoubleSplitComplex(realp: srcReals.baseAddress!,
                                          imagp: srcImaginaries.baseAddress!)
    
    
    let dstReals = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    let dstImaginaries = UnsafeMutableBufferPointer<Double>.allocate(capacity: n)
    
    var dstValues = DSPDoubleSplitComplex(realp: dstReals.baseAddress!,
                                          imagp: dstImaginaries.baseAddress!)
    
    vDSP_zvnegD(&srcValues, stride,
                &dstValues, stride,
                vDSP_Length(n))
    
    // Prints "[1.0, -2.0, 3.0, -4.0, 5.0, -6.0, 7.0, -8.0]".
    print(Array(dstReals))
    
    // Prints "[-10.0, -20.0, -30.0, -40.0, 50.0, 60.0, 70.0, 80.0]".
    print(Array(dstImaginaries))
```

## Parameters

- `__A`: The input vector  .
- `__IA`: The distance between the elements in the input vector  .
- `__C`: On output, the negative values of the elements in the input vector.
- `__IC`: The distance between the elements in the output vector  .
- `__N`: The number of elements that the function processes.

## See Also

- [vDSP_zvneg](vdsp_zvneg.md)
  Calculates the negative value of each element in the supplied complex single-precision vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zvnegd)*