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
| 3 | 8 | **8** |
| 4 | 16 | **16** |
| 5 | 32 | **32** |
| 6 | 64 | **64** |
| 7 | 128 | **128** |
| 8 | 256 | **256** |
| 9 | 512 | **512** |
| 10 | 1024 | **1024** |
| 11 | 2048 | **2048** |
| 12 | 4096 | **4096** |

##### Supported Lengths for F = 3

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 | **12** |
| 3 | 8 | **24** |
| 4 | 16 | **48** |
| 5 | 32 | **96** |
| 6 | 64 | **192** |
| 7 | 128 | **384** |
| 8 | 256 | **768** |

##### Supported Lengths for F = 5

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 | **20** |
| 3 | 8 | **40** |
| 4 | 16 | **80** |
| 5 | 32 | **160** |
| 6 | 64 | **320** |
| 7 | 128 | **640** |

##### Supported Lengths for F = 9

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 | **36** |
| 3 | 8 | **72** |
| 4 | 16 | **144** |
| 5 | 32 | **288** |
| 6 | 64 | **576** |
| 7 | 128 | **1152** |

##### Supported Lengths for F = 15

| n | `2ⁿ` | `length` (`f * 2ⁿ`) |
| --- | --- | --- |
| 2 | 4 | **60** |
| 3 | 8 | **120** |
| 4 | 16 | **240** |
| 5 | 32 | **480** |
| 6 | 64 | **960** |
| 7 | 128 | **1920** |

## Parameters

- `previous`: An existing [`vDSP.DiscreteFourierTransform`](vdsp/discretefouriertransform.md) structure that shares memory with the discrete Fourier transform instance that this function returns. Pass `nil` to create an object with newly initialized and allocated memory.
- `count`: The number of complex elements.
- `direction`: A flag that specifies the transform direction.
- `transformType`: A flag that specifies whether the forward transform is real-to-complex or complex-to-complex.
- `ofType`: The data type for the discrete Fourier transform operation. For split-complex operations, this needs to be be either [`Float`](https://developer.apple.com/documentation/Swift/Float) or [`Double`](https://developer.apple.com/documentation/Swift/Double). For interleaved operations, this needs to be either [`DSPComplex`](dspcomplex.md) or [`DSPDoubleComplex`](dspdoublecomplex.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/init(previous:count:direction:transformtype:oftype:))*