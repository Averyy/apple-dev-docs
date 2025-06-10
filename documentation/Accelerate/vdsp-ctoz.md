# vDSP_ctoz

**Framework**: Accelerate  
**Kind**: func

Copies the contents of an interleaved single-precision complex vector to a split complex vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_ctoz(const DSPComplex * __C, vDSP_Stride __IC, const DSPSplitComplex * __Z, vDSP_Stride __IZ, vDSP_Length __N);
```

## Mentions

- [Understanding data packing for Fourier transforms](understanding-data-packing-for-fourier-transforms.md)
- [Performing Fourier transforms on interleaved-complex data](performing-fourier-transforms-on-interleaved-complex-data.md)
- [Controlling vDSP operations with stride](controlling-vdsp-operations-with-stride.md)

#### Discussion

For example, the following code converts the contents of an array of [`DSPComplex`](dspcomplex.md) structures to a [`DSPSplitComplex`](dspsplitcomplex.md) structure:

```swift
    let source: [DSPComplex] = [
        DSPComplex(real: 1.0, imag: 10.0),
        DSPComplex(real: 2.0, imag: 20.0),
        DSPComplex(real: 3.0, imag: 30.0),
        DSPComplex(real: 4.0, imag: 40.0),
    ]
    
    let destReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    let destImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
    
    var destination = DSPSplitComplex(realp: destReal.baseAddress!,
                                      imagp: destImag.baseAddress!)
    
    vDSP_ctoz(source, 2,
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

- [vDSP_ctozD](vdsp_ctozd.md)
  Copies the contents of an interleaved double-precision complex vector to a split complex vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_ctoz)*