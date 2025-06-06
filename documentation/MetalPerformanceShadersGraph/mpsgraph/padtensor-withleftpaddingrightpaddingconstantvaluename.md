# padTensor(_:with:leftPadding:rightPadding:constantValue:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a padding operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func padTensor(_ tensor: MPSGraphTensor, with paddingMode: MPSGraphPaddingMode, leftPadding: [NSNumber], rightPadding: [NSNumber], constantValue: Double, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `tensor`: The input tensor.
- `paddingMode`: The parameter that defines the padding mode.
- `leftPadding`: The parameter that defines how much padding the operation applies to the input tensor before each dimension - must be of size  .
- `rightPadding`: The parameter that defines how much padding the operation applies to the input tensor after each dimension - must be of size  .
- `constantValue`: The constant value the operation uses when  .
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/padtensor(_:with:leftpadding:rightpadding:constantvalue:name:))*