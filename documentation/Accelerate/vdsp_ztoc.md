# vDSP_ztoc

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Copies the contents of a split single-precision complex vector to an interleaved vector.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void vDSP_ztoc(const DSPSplitComplex *__Z, vDSP_Stride __IZ, DSPComplex *__C, vDSP_Stride __IC, vDSP_Length __N);
```

## Mentions

- [Performing Fourier transforms on interleaved-complex data](./performing-fourier-transforms-on-interleaved-complex-data.md)
- [Controlling vDSP operations with stride](./controlling-vdsp-operations-with-stride.md)

#### Discussion

For example, the following code converts the contents of a [`DSPSplitComplex`](./dspsplitcomplex.md) structure to an array of [`DSPComplex`](./dspcomplex.md) structures :

**Swift**:

```swift
let srcReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
_ = srcReal.initialize(from: [1.0, 2.0, 3.0, 4.0])

let srcImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: 4)
_ = srcImag.initialize(from: [10.0, 20.0, 30.0, 40.0])

var source = DSPSplitComplex(realp: srcReal.baseAddress!,
                             imagp: srcImag.baseAddress!)

let destination = [DSPComplex](unsafeUninitializedCapacity: 4) {
    buffer, initializedCount in

    vDSP_ztoc(&source, 1,
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

**Objective-C**:

```objc
float srcRealp[4] = {1.0, 2.0, 3.0, 4.0};
float srcImagp[4] = {10.0, 20.0, 30.0, 40.0};
DSPSplitComplex source = { .realp = srcRealp, .imagp = srcImagp };

DSPComplex destination[4];

vDSP_ztoc(&source, 1,
          destination, 2,
          4);

// Prints "[DSPComplex(real: 1, imag: 10), DSPComplex(real: 2, imag: 20), DSPComplex(real: 3, imag: 30), DSPComplex(real: 4, imag: 40)]".
printf("[DSPComplex(real: %g, imag: %g), DSPComplex(real: %g, imag: %g), DSPComplex(real: %g, imag: %g), DSPComplex(real: %g, imag: %g)]\n",
      destination[0].real, destination[0].imag,
      destination[1].real, destination[1].imag,
      destination[2].real, destination[2].imag,
      destination[3].real, destination[3].imag);
```

## Parameters

- `__Z`: The split-complex input vector.
- `__IZ`: The distance between the elements in the input vector.
- `__C`: The interleaved-complex output vector.
- `__IC`: The distance between the real elements in the output vector. For example, a stride of `2` corresponds to a single complex element.
- `__N`: The number of complex elements that the function processes.

## See Also

### Converting split-complex vectors to interleaved-complex vectors
- [vDSP_ztocD](./vdsp_ztocd.md)
  Copies the contents of a split double-precision complex vector to an interleaved vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_ztoc)*