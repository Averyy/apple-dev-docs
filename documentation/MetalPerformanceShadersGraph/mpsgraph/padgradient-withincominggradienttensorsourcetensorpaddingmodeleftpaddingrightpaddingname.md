# padGradient(withIncomingGradientTensor:sourceTensor:paddingMode:leftPadding:rightPadding:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a padding gradient operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func padGradient(withIncomingGradientTensor incomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, paddingMode: MPSGraphPaddingMode, leftPadding: [NSNumber], rightPadding: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `incomingGradientTensor`: The input gradient tensor.
- `sourceTensor`: The input tensor of the forward pass.
- `paddingMode`: The parameter that defines the padding mode.
- `leftPadding`: The parameter that defines how much padding the operation applies to the input tensor before each dimension - must be of size  .
- `rightPadding`: The parameter that defines how much padding the operation applies to the input tensor after each dimension - must be of size  .
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/padgradient(withincominggradienttensor:sourcetensor:paddingmode:leftpadding:rightpadding:name:))*