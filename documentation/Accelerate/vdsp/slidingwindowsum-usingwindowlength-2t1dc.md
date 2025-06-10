# slidingWindowSum(_:usingWindowLength:)

**Framework**: Accelerate  
**Kind**: method

Returns the double-precision sliding window sum of a vector.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
static func slidingWindowSum<U>(_ vector: U, usingWindowLength windowLength: Int) -> [Double] where U : AccelerateBuffer, U.Element == Double
```

#### Discussion

Use this function to populate an output vector with the consecutive sums of values in a sliding window. The number of elements in the input vector must be one subtracted from the sum of the window length and the number of window positions.

The number of elements in the output vector must be the same as the number of elements in the input vector. This is because although the function only writes the number of window positions to the output vector, it may require additional elements for intermediate computation.

The following code shows how to compute the sums of values in a three-element sliding window moved through a ten-element array. The code processes every element in the input array, and the output result contains eight values.

```swift
let input: [Float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

var output = [Float](repeating: .nan,
                     count: input.count)

let windowLength = vDSP_Length(3)
let outputCount = vDSP_Length(input.count) - windowLength + 1
let stride = vDSP_Stride(1)

vDSP_vswsum(input, stride,
            &output, stride,
            outputCount,
            windowLength)

// Prints "[6.0, 9.0, 12.0, 15.0, 18.0, 21.0, 24.0, 27.0]"
print(output[0 ..< Int(outputCount)])
```

The figure below illustrates the process the function uses to calculate the result:

![A diagram that depicts the steps taken by the function to compute the sliding window sum. The diagram consists of eight stacked rows that represent each step. Each step in the process moves a three-element sliding window from left to right, and the value for each step is the sum of values in the sliding window.](https://docs-assets.developer.apple.com/published/5ae3e9651cc0da0638c748430b882cd4/media-4329493%402x.png)

Alternatively, the following code shows how to process input elements to generate a specific number of output elements. Use this technique, for example, to process streaming input data. The code below takes `count` elements from the input collection and returns the sums at eight window positions:

```swift
let input: [Float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                      11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                      21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
let inputPageNumber = 1

let windowLength = vDSP_Length(3)
let outputCount = vDSP_Length(8)

let count = Int(outputCount + windowLength - 1)

var output = [Float](repeating: .nan,
                     count: count)

let stride = vDSP_Stride(1)

input.withUnsafeBufferPointer { srcPtr in
    vDSP_vswsum((srcPtr.baseAddress!.advanced(by: count * inputPageNumber)),
                stride,
                &output, stride,
                outputCount,
                windowLength)
}

// Prints "[36.0, 39.0, 42.0, 45.0, 48.0, 51.0, 54.0, 57.0]".
print(output[0 ..< Int(outputCount)])
```

The figure below illustrates the process the function uses to calculate the result:

![A diagram that depicts the steps taken by the function to compute the sliding window sum. The diagram consists of eight stacked rows that represent each step. Each step in the process moves a three-element sliding window from left to right, and the value for each step is the sum of values in the sliding window.](https://docs-assets.developer.apple.com/published/064ef2a3762daf0a2c6c218aa2f13174/media-4329486%402x.png)

## Parameters

- `vector`: The input vector.
- `windowLength`: The length of the window, which must be greater than zero.

## See Also

- [static func slidingWindowSum<U>(U, usingWindowLength: Int) -> [Float]](vdsp/slidingwindowsum(_:usingwindowlength:)-reb8.md)
  Returns the single-precision sliding window sum of a vector.
- [static func slidingWindowSum<U, V>(U, usingWindowLength: Int, result: inout V)](vdsp/slidingwindowsum(_:usingwindowlength:result:)-i972.md)
  Calculates the double-precision sliding window sum of a vector.
- [static func slidingWindowSum<U, V>(U, usingWindowLength: Int, result: inout V)](vdsp/slidingwindowsum(_:usingwindowlength:result:)-5tg0h.md)
  Calculates the single-precision sliding window sum of a vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/slidingwindowsum(_:usingwindowlength:)-2t1dc)*