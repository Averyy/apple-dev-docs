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

## Parameters

- `previous`: An existing   structure that shares memory with the discrete Fourier transform instance that this function returns. Pass   to create an object with newly initialized and allocated memory.
- `count`: The number of complex elements. For split-complex real-to-complex, the value of count must be   or  , where   is  ,  , or   and  . For split-complex complex-to-complex, the value of count must be   or  , where   is  ,  , or   and  . And for interleaved, the value of count must be  , where   is  ,  ,  ,  ,  , or  , and  .
- `direction`: A flag that specifies the transform direction.
- `transformType`: A flag that specifies whether the forward transform is real-to-complex or complex-to-complex.
- `ofType`: The data type for the discrete Fourier transform operation. For split-complex operations, this must be either   or  . For interleaved operations, this must be either   or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vdsp/discretefouriertransform/init(previous:count:direction:transformtype:oftype:))*