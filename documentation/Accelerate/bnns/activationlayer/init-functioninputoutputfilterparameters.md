# init(function:input:output:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new activation layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
convenience init?(function activationFunction: BNNS.ActivationFunction, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The input dimensions must be equal to the output dimensions. For activation types other than identity, the input and output must be `float`.

## Parameters

- `activationFunction`: The activation function that the layer applies to the output.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationlayer/init(function:input:output:filterparameters:))*