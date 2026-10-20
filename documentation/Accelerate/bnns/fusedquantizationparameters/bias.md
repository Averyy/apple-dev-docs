# bias

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The descriptor of the bias.

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
var bias: BNNSNDArrayDescriptor?
```

## See Also

### Inspecting the Properties of a Fused Quantization Parameters Structure
- [var scale: BNNSNDArrayDescriptor?](./scale.md)
  The descriptor of the scale.
- [var axis: Int?](./axis.md)
  The index of the axis on which the function applies scale and bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedquantizationparameters/bias)*