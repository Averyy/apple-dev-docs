# vDSP_zconv

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs either correlation or convolution on two complex single-precision vectors.

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
extern void vDSP_zconv(const DSPSplitComplex *__A, vDSP_Stride __IA, const DSPSplitComplex *__F, vDSP_Stride __IF, const DSPSplitComplex *__C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __P);
```

#### Discussion

Use this function to compute either the convolution or the correlation of an input signal and a filter vector. Both operations compute the sliding dot product of the filter and the section of the input signal that the filter is over. Specify a positive stride through the filter to perform correlation and a negative stride through the filter to perform convolution. When you perform convolution, the `__F` parameter must point to the last element in the filter.

The function can run in place, but `C` can’t be in place with `F`. For example, the following code defines an input signal, a filter, and the number of output elements:

**Swift**:

```swift
let signalReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: 8)
_ = signalReal.initialize(from: [1, 2, 3, 4, 5, 6, 7, 8])

let signalImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: 8)
_ = signalImag.initialize(from: [1, 2, 3, 4, 5, 6, 7, 8])

var signal = DSPSplitComplex(realp: signalReal.baseAddress!,
                             imagp: signalImag.baseAddress!)

let filterReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: 3)
_ = filterReal.initialize(from: [10, 20, 30])

let filterImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: 3)
_ = filterImag.initialize(from: [10, 20, 30])

var filter = DSPSplitComplex(realp: filterReal.baseAddress!,
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

**Objective-C**:

```objc
float signalRealp[8] = {1, 2, 3, 4, 5, 6, 7, 8};
float signalImagp[8] = {1, 2, 3, 4, 5, 6, 7, 8};
DSPSplitComplex signal = { .realp = signalRealp, .imagp = signalImagp };

float filterRealp[3] = {10, 20, 30};
float filterImagp[3] = {10, 20, 30};
DSPSplitComplex filter = { .realp = filterRealp, .imagp = filterImagp };

vDSP_Length filterCount = 3;
vDSP_Length outputCount = 8 - 3 + 1;
```

##### Perform Correlation

The following code performs correlation. In this example, the stride through the filter is `1`:

**Swift**:

```swift
let correlationResultReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: outputCount)
let correlationResultImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: outputCount)
var correlationResult = DSPSplitComplex(realp: correlationResultReal.baseAddress!,
                                        imagp: correlationResultImag.baseAddress!)

defer {
    correlationResultReal.deallocate()
    correlationResultImag.deallocate()
}

vDSP_zconv(&signal,
          1,
          &filter,
          1, // The stride through the filter vector.
          &correlationResult,
          1,
          vDSP_Length(outputCount),
          vDSP_Length(filterCount))
```

**Objective-C**:

```objc
float corrRealp[6];
float corrImagp[6];
DSPSplitComplex correlationResult = { .realp = corrRealp, .imagp = corrImagp };

vDSP_zconv(&signal,
           1,
           &filter,
           1, // The stride through the filter vector.
           &correlationResult,
           1,
           outputCount,
           filterCount);
```

On return, `correlationResultReal` contains all zeroes and `correlationResultImag` contains the values `[280.0, 400.0, 520.0, 640.0, 760.0, 880.0]`. For example, the operation calculates the first element, `280`, as:

```c
(1 + 1i) * (10 + 10i) + (2 + 2i) * (20 + 20i) + (3 + 3i) * (30 + 30i) = 280
```

##### Perform Convolution

The following code performs convolution. In this example, the stride through the filter is `-1` and the filter parameter points to the last element in the filter:

**Swift**:

```swift
let convolutionResultReal = UnsafeMutableBufferPointer<Float>.allocate(capacity: outputCount)
let convolutionResultImag = UnsafeMutableBufferPointer<Float>.allocate(capacity: outputCount)
var convolutionResult = DSPSplitComplex(realp: convolutionResultReal.baseAddress!,
                                        imagp: convolutionResultImag.baseAddress!)

defer {
    convolutionResultReal.deallocate()
    convolutionResultImag.deallocate()
}

var kernel = DSPSplitComplex(realp: filter.realp.advanced(by: filterCount - 1),
                             imagp: filter.imagp.advanced(by: filterCount - 1))

vDSP_zconv(&signal,
           1,
           &kernel,
           -1, // The stride through the filter vector.
           &convolutionResult,
           1,
           vDSP_Length(outputCount),
           vDSP_Length(filterCount))

print("convolutionResult r", Array(convolutionResultReal))
print("convolutionResult i", Array(convolutionResultImag))
```

**Objective-C**:

```objc
float convRealp[6];
float convImagp[6];
DSPSplitComplex convolutionResult = { .realp = convRealp, .imagp = convImagp };

DSPSplitComplex kernel = {
    .realp = filterRealp + filterCount - 1,
    .imagp = filterImagp + filterCount - 1
};

vDSP_zconv(&signal,
           1,
           &kernel,
           -1, // The stride through the filter vector.
           &convolutionResult,
           1,
           outputCount,
           filterCount);

// Prints "convolutionResult r [0, 0, 0, 0, 0, 0]".
//         convolutionResult i [200, 320, 440, 560, 680, 800]
printf("convolutionResult r [%g, %g, %g, %g, %g, %g]\n",
      convRealp[0], convRealp[1], convRealp[2],
      convRealp[3], convRealp[4], convRealp[5]);
printf("convolutionResult i [%g, %g, %g, %g, %g, %g]\n",
      convImagp[0], convImagp[1], convImagp[2],
      convImagp[3], convImagp[4], convImagp[5]);
```

On return, `correlationResultReal` contains all zeroes and `correlationResultImag` contains the values `[200.0, 320.0, 440.0, 560.0, 680.0, 800.0]`. For example, the operation calculates the first element, `200`, as:

```c
(1 + 1i) * (30 + 30i) + (2 + 2i) * (20 + 20i) + (3 + 3i) * (10 + 10i) = 200
```

## Parameters

- `__A`: The complex single-precision input signal vector. The length of this vector must be at least `N + P - 1`.
- `__IA`: The stride through the input signal vector, `A`.
- `__F`: The complex single-precision filter vector.
- `__IF`: The stride through the filter vector, `F`.
- `__C`: The complex single-precision output signal vector.
- `__IC`: The stride through the output signal vector, `C`.
- `__N`: The number of elements in the output signal vector, `C`.
- `__P`: The number of elements in the filter vector, `F`.

## See Also

### Complex Vectors
- [vDSP_zconvD](./vdsp_zconvd.md)
  Performs either correlation or convolution on two complex double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_zconv)*