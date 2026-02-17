# init(previous:count:direction:transformType:ofType:)

**Framework**: Accelerate  
**Kind**: init

Returns a new discrete Fourier transform instance.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
init(previous: vDSP.DiscreteFourierTransform<Float>? = nil, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType, ofType: T.Type) throws
```

#### Discussion

The interleaved DFT operations that the Accelerate framework provides work over collections with specific counts. The maximum number of complex elements that these operations support is 4096, and other supported counts are the result of the formula `f * 2ⁿ` for certain values of `f` and `n`. In the case of real-to-complex, `n` is the number of real elements divided by two, and for complex-to-complex `n` is the number of complex elements.

The following tables show the complete list of supported lengths for different values of `f` and `n`:

##### Supported Lengths for F = 1

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |
| 8 | 256 |  |
| 9 | 512 |  |
| 10 | 1024 |  |
| 11 | 2048 |  |
| 12 | 4096 |  |

##### Supported Lengths for F = 3

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |
| 8 | 256 |  |

##### Supported Lengths for F = 5

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |

##### Supported Lengths for F = 9

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |

##### Supported Lengths for F = 15

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 |  |
| 3 | 8 |  |
| 4 | 16 |  |
| 5 | 32 |  |
| 6 | 64 |  |
| 7 | 128 |  |

## Parameters

- `previous`: An existing   structure that shares memory with the discrete Fourier transform instance that this function returns. Pass   to create an object with newly initialized and allocated memory.
- `count`: The number of complex elements.
- `direction`: A flag that specifies the transform direction.
- `transformType`: A flag that specifies whether the forward transform is real-to-complex or complex-to-complex.
- `ofType`: The data type for the discrete Fourier transform operation. For split-complex operations, this needs to be be either   or  . For interleaved operations, this needs to be either   or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/init(previous:count:direction:transformtype:oftype:))*