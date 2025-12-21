# init(inputA:inputADescriptorType:inputB:inputBDescriptorType:inputC:inputCDescriptorType:output:outputDescriptorType:function:activation:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new ternary arithmetic layer.

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
convenience init?(inputA: BNNSNDArrayDescriptor, inputADescriptorType: BNNS.DescriptorType, inputB: BNNSNDArrayDescriptor, inputBDescriptorType: BNNS.DescriptorType, inputC: BNNSNDArrayDescriptor, inputCDescriptorType: BNNS.DescriptorType, output: BNNSNDArrayDescriptor, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticTernaryFunction, activation: BNNS.ActivationFunction = .identity, filterParameters: BNNSFilterParameters? = nil)
```

## Parameters

- `inputA`: The first input descriptor.
- `inputADescriptorType`: The first input descriptor type.
- `inputB`: The second input descriptor.
- `inputBDescriptorType`: The second input descriptor type.
- `inputC`: The first third descriptor.
- `inputCDescriptorType`: The third input descriptor type.
- `output`: The output descriptor.
- `outputDescriptorType`: The output descriptor type.
- `function`: The arithmetic function.
- `activation`: The activation function that the layer applies to the output.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/ternaryarithmeticlayer/init(inputa:inputadescriptortype:inputb:inputbdescriptortype:inputc:inputcdescriptortype:output:outputdescriptortype:function:activation:filterparameters:))*