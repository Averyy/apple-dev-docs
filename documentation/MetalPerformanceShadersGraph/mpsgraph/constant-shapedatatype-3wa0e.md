# constant(_:shape:dataType:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a constant op with a given shape and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func constant(_ scalar: Double, shape: [NSNumber], dataType: MPSDataType) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `scalar`: The scalar value to fill the entire tensor values with.
- `shape`: The shape of the output tensor.
- `dataType`: The dataType of the constant tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/constant(_:shape:datatype:)-3wa0e)*