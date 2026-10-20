# epsilon

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The epsilon in the computation of the standard deviation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
var epsilon: Float
```

## See Also

### Inspecting the Properties of a Fused Normalization Parameters Structure
- [var type: BNNS.NormalizationType](./type.md)
  An enumeration that specifies the normalization type.
- [var beta: BNNSNDArrayDescriptor?](./beta.md)
  The descriptor of the beta.
- [var gamma: BNNSNDArrayDescriptor?](./gamma.md)
  The descriptor of the gamma.
- [var momentum: Float](./momentum.md)
  A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- [var activation: BNNS.ActivationFunction](./activation.md)
  The activation function that the layer applies to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusednormalizationparameters/epsilon)*