# placeholder(shape:dataType:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a placeholder operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func placeholder(shape: [NSNumber]?, dataType: MPSDataType, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `shape`: The shape of the output tensor. A nil shape will result in an unranked tensor.
- `dataType`: The dataType of the placeholder tensor.
- `name`: The name for the placeholder operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/placeholder(shape:datatype:name:))*