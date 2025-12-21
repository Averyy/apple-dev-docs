# init(type:beta:gamma:momentum:epsilon:activation:)

**Framework**: Accelerate  
**Kind**: init

Returns a new fused normalization parameters structure.

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
init(type: BNNS.NormalizationType, beta: BNNSNDArrayDescriptor? = nil, gamma: BNNSNDArrayDescriptor? = nil, momentum: Float = 0, epsilon: Float, activation: BNNS.ActivationFunction)
```

## Parameters

- `type`: An enumeration that specifies the normalization type.
- `beta`: The descriptor of the beta.
- `gamma`: The descriptor of the gamma.
- `momentum`: A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- `epsilon`: The epsilon in the computation of the standard deviation.
- `activation`: The activation function that the layer applies to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusednormalizationparameters/init(type:beta:gamma:momentum:epsilon:activation:))*