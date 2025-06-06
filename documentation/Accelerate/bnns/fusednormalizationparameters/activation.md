# activation

**Framework**: Accelerate  
**Kind**: property

The activation function that the layer applies to the output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
var activation: BNNS.ActivationFunction
```

## See Also

- [var type: BNNS.NormalizationType](bnns/fusednormalizationparameters/type.md)
  An enumeration that specifies the normalization type.
- [var beta: BNNSNDArrayDescriptor?](bnns/fusednormalizationparameters/beta.md)
  The descriptor of the beta.
- [var gamma: BNNSNDArrayDescriptor?](bnns/fusednormalizationparameters/gamma.md)
  The descriptor of the gamma.
- [var momentum: Float](bnns/fusednormalizationparameters/momentum.md)
  A value, between 0 and 1, the normalization operation uses to update the moving mean and moving variance during training.
- [var epsilon: Float](bnns/fusednormalizationparameters/epsilon.md)
  The epsilon in the computation of the standard deviation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusednormalizationparameters/activation)*