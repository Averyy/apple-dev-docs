# init(previousDFT:count:direction:transformType:ofType:)

**Framework**: Accelerate  
**Kind**: init

Initializes a new discrete Fourier transform structure.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS ?+
- watchOS 26.0+

## Declaration

```swift
init(previousDFT: vDSP.DiscreteFourierTransform<T>?, count: Int, direction: vDSP.FourierTransformDirection, transformType: vDSP.DFTTransformType, ofType: T.Type) throws
```

#### Discussion

The `count` parameter must be:

- For split-complex real-to-complex: `2ⁿ` or `f * 2ⁿ`, where `f` is `3`, `5`, or `15` and `n >= 4`.
- For split-complex complex-to-complex: `2ⁿ` or `f * 2ⁿ`, where `f` is `3`, `5`, or `15` and `n >= 3`.
- For interleaved: `f * 2ⁿ`, where `f` is `2`, `3`, `5`, `3x3`, `3x5`, or `5x5`, and `n>=2`.

## Parameters

- `previousDFT`: A previous DFT instance to share data with.
- `count`: The number of complex elements.
- `transformType`: Specifies whether the forward transform is real-to-complex or complex-to-complex.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/init(previousdft:count:direction:transformtype:oftype:))*