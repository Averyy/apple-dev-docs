# init(scale:bias:)

**Framework**: Accelerate  
**Kind**: init

Returns a new fused quantization parameters structure.

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
init(scale: BNNSNDArrayDescriptor?, bias: BNNSNDArrayDescriptor?)
```

## Parameters

- `scale`: The descriptor of the scale.
- `bias`: The descriptor of the bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedquantizationparameters/init(scale:bias:))*