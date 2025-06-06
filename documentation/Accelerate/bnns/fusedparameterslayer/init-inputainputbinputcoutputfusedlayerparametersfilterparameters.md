# init(inputA:inputB:inputC:output:fusedLayerParameters:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Creates a new fused layer from an array of layer parameters, where the first layer accepts three inputs.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `inputA`: The descriptor of the first input.
- `inputB`: The descriptor of the second input.
- `inputC`: The descriptor of the third input.
- `output`: The descriptor of the output.
- `fusedLayerParameters`: An array that contains the parameters of the fused layers.
- `filterParameters`: The runtime filter parameters.

## See Also

- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](bnns/fusedparameterslayer/init(input:output:fusedlayerparameters:filterparameters:).md)
  Creates a new fused layer from an array of layer parameters.
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](bnns/fusedparameterslayer/init(inputa:inputb:output:fusedlayerparameters:filterparameters:).md)
  Creates a new fused layer from an array of layer parameters, where the first layer accepts two inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedparameterslayer/init(inputa:inputb:inputc:output:fusedlayerparameters:filterparameters:))*