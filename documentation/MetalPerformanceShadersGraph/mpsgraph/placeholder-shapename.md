# placeholder(shape:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a placeholder operation and returns the result tensor with the dataType of the placeholder tensor set to 32 bit float.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func placeholder(shape: [NSNumber]?, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `shape`: The shape of the output tensor. A nil shape will result in an unranked tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/placeholder(shape:name:))*