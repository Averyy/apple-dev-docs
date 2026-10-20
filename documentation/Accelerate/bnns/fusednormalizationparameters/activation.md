# activation

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The activation function that the layer applies to the output.

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
var activation: BNNS.ActivationFunction
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
- [var epsilon: Float](./epsilon.md)
  The epsilon in the computation of the standard deviation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusednormalizationparameters/activation)*