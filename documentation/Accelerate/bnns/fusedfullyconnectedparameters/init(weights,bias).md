# init(weights:bias:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new fused dequantization parameters structure.

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
init(weights: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?)
```

## Parameters

- `weights`: The descriptor of the weights.
- `bias`: The descriptor of the bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedfullyconnectedparameters/init(weights:bias:))*