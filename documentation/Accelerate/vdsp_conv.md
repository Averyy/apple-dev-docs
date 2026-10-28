# vDSP_conv

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs either correlation or convolution on two real single-precision vectors.

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
extern void vDSP_conv(const float *__A, vDSP_Stride __IA, const float *__F, vDSP_Stride __IF, float *__C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __P);
```

## Mentions

- [Controlling vDSP operations with stride](./controlling-vdsp-operations-with-stride.md)

## Discussion

Use this function to compute either the convolution or the correlation of an input signal and a filter vector. Both operations compute the sliding dot product of the filter and the section of the input signal that the filter is over. Specify a positive stride through the filter to perform correlation and a negative stride through the filter to perform convolution. When you perform convolution, the `__F` parameter must point to the last element in the filter.

The function can run in place, but `C` can’t be in place with `F`. For example, the following code defines an input signal, a filter, and the number of output elements:

```swift
let signal: [Float] = [1, 2, 3, 4, 5, 6, 7, 8]

let filter: [Float] = [10, 20, 30]

let outputCount = signal.count - filter.count + 1
```

### Perform Correlation

The following code performs correlation. In this example, the stride through the filter is `1`:

**Swift**:

```swift
var correlationResult = [Float](repeating: 0,
                                count: outputCount)

vDSP_conv(signal,
          1, // Stride through the `signal` vector.
          filter,
          1, // Stride through the `filter` vector: `1` for correlation.
          &correlationResult,
          1, // Stride through the `correlationResult` vector.
          vDSP_Length(outputCount),
          vDSP_Length(filter.count))
```

**Objective-C**:

```objc
float signal[8] = {1, 2, 3, 4, 5, 6, 7, 8};
float filter[3] = {10, 20, 30};
vDSP_Length outputCount = 6;

float correlationResult[6] = {0};

vDSP_conv(signal, 1,             // Stride through the `signal` vector.
          filter, 1,             // Stride through the `filter` vector: `1` for correlation.
          correlationResult, 1,  // Stride through the `correlationResult` vector.
          outputCount,
          3);

// Prints "[140, 200, 260, 320, 380, 440]".
printf("[%g, %g, %g, %g, %g, %g]\n",
      correlationResult[0], correlationResult[1], correlationResult[2],
      correlationResult[3], correlationResult[4], correlationResult[5]);
```

On return, `correlationResult` contains the values `[140.0, 200.0, 260.0, 320.0, 380.0, 440.0]`. The figure below shows how the function calculates each element in the result:

![A block diagram of a correlation operation. The top row represents the input signal and contains eight cells numbered one through eight. The six subsequent rows represent the output elements that the function calculates from the three-element filter sliding from left to right. For example, the bottom row represents the last output element and aligns with the input cells six, seven, and eight. The value of the last  output element is the sum of six times ten, seven times twenty, and eight times thirty, where ten, twenty, and thirty are the three filter elements.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3920909@2x.png)

### Perform Convolution

The following code performs convolution. In this example, the stride through the filter is `-1` and the filter parameter points to the last element in the filter:

**Swift**:

```swift
var convolutionResult = [Float](repeating: 0,
                                count: outputCount)

filter.withUnsafeBufferPointer { filterPtr in
    vDSP_conv(signal,
              1, // Stride through the `signal` vector.
              filterPtr.baseAddress!.advanced(by: filter.count - 1),
              -1, // Stride through the `filter` vector: `-1` for convolution.
              &convolutionResult,
              1, // Stride through the `convolutionResult` vector.
              vDSP_Length(outputCount),
              vDSP_Length(filter.count))
}
```

**Objective-C**:

```objc
float signal[8] = {1, 2, 3, 4, 5, 6, 7, 8};
float filter[3] = {10, 20, 30};
vDSP_Length outputCount = 6;

float convolutionResult[6] = {0};

// For convolution: pass stride `-1` and a pointer to the last filter element.
vDSP_conv(signal, 1,            // Stride through the `signal` vector.
          &filter[2], -1,       // Stride through the `filter` vector: `-1` for convolution.
          convolutionResult, 1, // Stride through the `convolutionResult` vector.
          outputCount,
          3);

// Prints "[100, 160, 220, 280, 340, 400]".
printf("[%g, %g, %g, %g, %g, %g]\n",
      convolutionResult[0], convolutionResult[1], convolutionResult[2],
      convolutionResult[3], convolutionResult[4], convolutionResult[5]);
```

On return, `convolutionResult` contains the values `[100.0, 160.0, 220.0, 280.0, 340.0, 400.0]`. The figure below shows how the function calculates each element in the result:

![A block diagram of a convolution operation. The top row represents the input signal and contains eight cells numbered one through eight. The six subsequent rows represent the output elements that the function calculates from the three-element filter sliding from left to right. For example, the bottom row represents the last output element and aligns with the input cells six, seven, and eight. The value of the last  output element is the sum of six times thirty, seven times twenty, and eight times ten, where thirty, twenty, and ten are the three filter elements with a negative stride.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3920915@2x.png)

## Parameters

- `__A`: The real single-precision input signal vector. The length of this vector must be at least `N + P - 1`.
- `__IA`: The stride through the input signal vector, `A`.
- `__F`: The real single-precision filter vector.
- `__IF`: The stride through the filter vector, `F`.
- `__C`: The real single-precision output signal vector.
- `__IC`: The stride through the output signal vector, `C`.
- `__N`: The number of elements in the output signal vector, `C`.
- `__P`: The number of elements in the filter vector, `F`.

## See Also

### Real Vectors
- [vDSP_convD](./vdsp_convd.md)
  Performs either correlation or convolution on two real double-precision vectors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_conv)*