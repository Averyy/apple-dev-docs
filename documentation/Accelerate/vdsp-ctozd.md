# vDSP_ctozD

**Framework**: Accelerate  
**Kind**: func

Copies the contents of an interleaved double-precision complex vector to a split complex vector.

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
extern void vDSP_ctozD(const DSPDoubleComplex * __C, vDSP_Stride __IC, const DSPDoubleSplitComplex * __Z, vDSP_Stride __IZ, vDSP_Length __N);
```

#### Discussion

For example, the following code converts the contents of an array of [`DSPDoubleComplex`](dspdoublecomplex.md) structures to a [`DSPDoubleSplitComplex`](dspdoublesplitcomplex.md) structure:

```swift
    let source: [DSPDoubleComplex] = [
        DSPDoubleComplex(real: 1.0, imag: 10.0),
        DSPDoubleComplex(real: 2.0, imag: 20.0),
        DSPDoubleComplex(real: 3.0, imag: 30.0),
        DSPDoubleComplex(real: 4.0, imag: 40.0),
    ]
    
    let destReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: 4)
    let destImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: 4)
    
    var destination = DSPDoubleSplitComplex(realp: destReal.baseAddress!,
                                            imagp: destImag.baseAddress!)
    
    vDSP_ctozD(source, 2, 
               &destination, 1,
               4)
    
    print(Array(destReal)) // Prints "[1.0, 2.0, 3.0, 4.0]".
    print(Array(destImag)) // Prints "[10.0, 20.0, 30.0, 40.0]".
```

## Parameters

- `__C`: The interleaved-complex input vector.
- `__IC`: The distance between the real elements in the input vector. For example, a stride of   corresponds to a single complex element.
- `__Z`: The split-complex output vector.
- `__IZ`: The distance between the elements in the ouput vector.
- `__N`: The number of complex elements that the function processes.

## See Also

- [vDSP_ctoz](vdsp_ctoz.md)
  Copies the contents of an interleaved single-precision complex vector to a split complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_ctozd)*