# vDSP_zconvD

**Framework**: Accelerate  
**Kind**: func

Performs either correlation or convolution on two complex double-precision vectors.

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
extern void vDSP_zconvD(const DSPDoubleSplitComplex * __A, vDSP_Stride __IA, const DSPDoubleSplitComplex * __F, vDSP_Stride __IF, const DSPDoubleSplitComplex * __C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

Use this function to compute either the convolution or the correlation of an input signal and a filter vector. Both operations compute the sliding dot product of the filter and the section of the input signal that the filter is over. Specify a positive stride through the filter to perform correlation and a negative stride through the filter to perform convolution. When you perform convolution, the `__F` parameter must point to the last element in the filter.

The function can run in place, but `C` can’t be in place with `F`. For example, the following code defines an input signal, a filter, and the number of output elements:

```swift
let signalReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: 8)
_ = signalReal.initialize(from: [1, 2, 3, 4, 5, 6, 7, 8])

let signalImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: 8)
_ = signalImag.initialize(from: [1, 2, 3, 4, 5, 6, 7, 8])

var signal = DSPDoubleSplitComplex(realp: signalReal.baseAddress!,
                                   imagp: signalImag.baseAddress!)

let filterReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: 3)
_ = filterReal.initialize(from: [10, 20, 30])

let filterImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: 3)
_ = filterImag.initialize(from: [10, 20, 30])

var filter = DSPDoubleSplitComplex(realp: filterReal.baseAddress!,
                                   imagp: filterImag.baseAddress!)
let filterCount = filterReal.count

let outputCount = signalReal.count - filterReal.count + 1

defer {
    signalReal.deallocate()
    signalImag.deallocate()
    filterReal.deallocate()
    filterImag.deallocate()
}
```

##### Perform Correlation

The following code performs correlation. In this example, the stride through the filter is `1`.

```swift
let correlationResultReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: outputCount)
let correlationResultImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: outputCount)
var correlationResult = DSPDoubleSplitComplex(realp: correlationResultReal.baseAddress!,
                                              imagp: correlationResultImag.baseAddress!)

defer {
    correlationResultReal.deallocate()
    correlationResultImag.deallocate()
}

vDSP_zconvD(&signal,
            1,
            &filter,
            1, // The stride through the filter vector.
            &correlationResult,
            1,
            vDSP_Length(outputCount),
            vDSP_Length(filterCount))
```

On return, `correlationResultReal` contains all zeroes and `correlationResultImag` contains the values `[280.0, 400.0, 520.0, 640.0, 760.0, 880.0]`. For example, the operation calculates the first element, `280`, as:

```c
(1 + 1i) * (10 + 10i) + (2 + 2i) * (20 + 20i) + (3 + 3i) * (30 + 30i) = 280
```

##### Perform Convolution

The following code performs convolution. In this example, the stride through the filter is `-1` and the filter parameter points to the last element in the filter.

```swift
let convolutionResultReal = UnsafeMutableBufferPointer<Double>.allocate(capacity: outputCount)
let convolutionResultImag = UnsafeMutableBufferPointer<Double>.allocate(capacity: outputCount)
var convolutionResult = DSPDoubleSplitComplex(realp: convolutionResultReal.baseAddress!,
                                        imagp: convolutionResultImag.baseAddress!)

defer {
    convolutionResultReal.deallocate()
    convolutionResultImag.deallocate()
}

var kernel = DSPDoubleSplitComplex(realp: filter.realp.advanced(by: filterCount - 1),
                                   imagp: filter.imagp.advanced(by: filterCount - 1))

vDSP_zconvD(&signal,
            1,
            &kernel,
            -1, // The stride through the filter vector.
            &convolutionResult,
            1,
            vDSP_Length(outputCount),
            vDSP_Length(filterCount))
```

On return, `correlationResultReal` contains all zeroes and `correlationResultImag` contains the values `[200.0, 320.0, 440.0, 560.0, 680.0, 800.0]`. For example, the operation calculates the first element, `200`, as:

```c
(1 + 1i) * (30 + 30i) + (2 + 2i) * (20 + 20i) + (3 + 3i) * (10 + 10i) = 200
```

## Parameters

- `__A`: The complex double-precision input signal vector. The length of this vector must be at least  .
- `__IA`: The stride through the input signal vector,  .
- `__F`: The complex double-precision filter vector.
- `__IF`: The stride through the filter vector,  .
- `__C`: The complex double-precision output signal vector.
- `__IC`: The stride through the output signal vector,  .
- `__N`: The number of elements in the output signal vector,  .
- `__P`: The number of elements in the filter vector,  .

## See Also

- [vDSP_zconv](vdsp_zconv.md)
  Performs either correlation or convolution on two complex single-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zconvd)*