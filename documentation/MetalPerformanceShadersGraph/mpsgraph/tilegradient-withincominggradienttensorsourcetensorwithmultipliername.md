# tileGradient(withIncomingGradientTensor:sourceTensor:withMultiplier:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a tile gradient operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func tileGradient(withIncomingGradientTensor incomingGradientTensor: MPSGraphTensor, sourceTensor: MPSGraphTensor, withMultiplier multiplier: [NSNumber], name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `incomingGradientTensor`: The input gradient tensor.
- `sourceTensor`: The input tensor of the forward pass.
- `multiplier`: An array of numbers that specifies how many copies per dimension MPSGraph produced in the forward pass.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/tilegradient(withincominggradienttensor:sourcetensor:withmultiplier:name:))*