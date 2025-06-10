# vDSP_vswmax

**Framework**: Accelerate  
**Kind**: func

Finds the maximum value in a sliding window at each possible position in a single-precision input vector.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
extern void vDSP_vswmax(const float * __A, vDSP_Stride __IA, float * __C, vDSP_Stride __IC, vDSP_Length __N, vDSP_Length __WindowLength);
```

#### Discussion

Use this function to populate an output vector with the consecutive maximum values in a sliding window. The number of elements in the input vector must be one subtracted from the sum of the window length and the number of window positions.

The number of elements in the output vector must be the same as the number of elements in the input vector. This is because although the function only writes the number of window positions to the output vector, it may require additional elements for intermediate computation.

The following code shows how to compute the maximum values in a five-element sliding window moved through a ten-element array. The output result contains six values.

```swift
let input: [Float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

var output = [Float](repeating: .nan,
                     count: input.count)

let windowLength = vDSP_Length(5)
let outputCount = vDSP_Length(input.count) - windowLength + 1
let stride = vDSP_Stride(1)

vDSP_vswmax(input, stride,
            &output, stride,
            outputCount,
            windowLength)

// Prints "[5.0, 6.0, 7.0, 8.0, 9.0, 10.0]".
print(output[0 ..< Int(outputCount)])
```

The figure below illustrates the process the function uses to calculate the result:

![A diagram that depicts the steps taken by the function to compute the sliding window maximum. The diagram consists of six stacked rows that represent each step. Each step in the process moves a five-element sliding window from left to right, and the value for each step is the maximum value in the sliding window.](https://docs-assets.developer.apple.com/published/029353a6fc3c3b40f3c1d4d9175af183/media-3738159%402x.png)

Alternatively, the following code shows how to process input elements to generate a specific number of output elements. Use this technique, for example, to process streaming input data. The code below takes `count` elements from the input collection and returns the maximum values at six window positions:

```swift
let input: [Float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                      21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
let inputPageNumber = 1

let windowLength = vDSP_Length(5)
let outputCount = vDSP_Length(6)

let count = Int(outputCount + windowLength - 1)

var output = [Float](repeating: .nan,
                     count: count)

let stride = vDSP_Stride(1)

input.withUnsafeBufferPointer { srcPtr in
    vDSP_vswmax((srcPtr.baseAddress!.advanced(by: count * inputPageNumber)),
                stride,
                &output, stride,
                outputCount,
                windowLength)
}

// Prints "[15.0, 16.0, 17.0, 18.0, 19.0, 20.0]"
print(output[0 ..< Int(outputCount)])
```

The figure below illustrates the process the function uses to calculate the result:

![A diagram that depicts the steps taken by the function to compute the sliding window maximum. The diagram consists of six stacked rows that represent each step. Each step in the process moves a five-element sliding window from left to right, and the value for each step is the maximum value in the sliding window.](https://docs-assets.developer.apple.com/published/9f85e886dede3c7039702c9cfd03e9e4/media-3738154%402x.png)

## Parameters

- `__A`: The input vector.
- `__IA`: The input stride, which is the distance between the elements in the input vector in which this function accesses elements.
- `__C`: The output vector.
- `__IC`: The input stride, which is the distance between the elements in the output vector in which this function accesses elements.
- `__N`: The number of output values, which is the same as the number of window positions the operation uses.
- `__WindowLength`: The length of the window, which must be greater than zero.

## See Also

- [vDSP_vswmaxD](vdsp_vswmaxd.md)
  Finds the maximum value in a sliding window at each possible position in a double-precision input vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp_vswmax)*