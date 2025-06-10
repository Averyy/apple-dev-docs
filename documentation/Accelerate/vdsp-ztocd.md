# vDSP_ztocD

**Framework**: Accelerate  
**Kind**: func

Copies the contents of a split double-precision complex vector to an interleaved vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_ztocD(const DSPDoubleSplitComplex * __Z, vDSP_Stride __IZ, DSPDoubleComplex * __C, vDSP_Stride __IC, vDSP_Length __N);
```

#### Discussion

For example, the following code converts the contents of a [`DSPDoubleSplitComplex`](dspdoublesplitcomplex.md) structure to an array of [`DSPDoubleComplex`](dspdoublecomplex.md) structures :

```swift
    let srcReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: 4)
    _ = srcReal.initialize(from: [1.0, 2.0, 3.0, 4.0])
    
    let srcImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: 4)
    _ = srcImag.initialize(from: [10.0, 20.0, 30.0, 40.0])
    
    var source = DSPDoubleSplitComplex(realp: srcReal.baseAddress!,
                                       imagp: srcImag.baseAddress!)
    
    let destination = [DSPDoubleComplex](unsafeUninitializedCapacity: 4) {
        buffer, initializedCount in
        
        vDSP_ztocD(&source, 1,
                   buffer.baseAddress!, 2,
                   4)
        
        initializedCount = 4
    }
    
    // Prints:
    //     "[ DSPComplex(real: 1.0, imag: 10.0),
    //        DSPComplex(real: 2.0, imag: 20.0),
    //        DSPComplex(real: 3.0, imag: 30.0),
    //        DSPComplex(real: 4.0, imag: 40.0) ]".
    print(destination)
```

## Parameters

- `__Z`: The split-complex input vector.
- `__IZ`: The distance between the elements in the input vector.
- `__C`: The interleaved-complex output vector.
- `__IC`: The distance between the real elements in the output vector. For example, a stride of   corresponds to a single complex element.
- `__N`: The number of complex elements that the function processes.

## See Also

- [vDSP_ztoc](vdsp_ztoc.md)
  Copies the contents of a split single-precision complex vector to an interleaved vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_ztocd)*