# init(input:output:fusedLayerParameters:filterParameters:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a new fused layer from an array of layer parameters.

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
convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `fusedLayerParameters`: An array that contains the parameters of the fused layers.
- `filterParameters`: The runtime filter parameters.

## See Also

### Creating a Fused Parameters Layer
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](./init%28inputa,inputb,output,fusedlayerparameters,filterparameters%29.md)
  Creates a new fused layer from an array of layer parameters, where the first layer accepts two inputs.
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](./init%28inputa,inputb,inputc,output,fusedlayerparameters,filterparameters%29.md)
  Creates a new fused layer from an array of layer parameters, where the first layer accepts three inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedparameterslayer/init(input:output:fusedlayerparameters:filterparameters:))*