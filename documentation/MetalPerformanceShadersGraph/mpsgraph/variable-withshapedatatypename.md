# variable(with:shape:dataType:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a variable operation and returns the result tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func variable(with data: Data, shape: [NSNumber], dataType: MPSDataType, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

## Parameters

- `data`: The data for the tensor. The number of bytes should be sizeof(dataType)numberOfElements.
- `shape`: The shape of the output tensor. This has to be statically shaped.
- `dataType`: The dataType of the constant tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/variable(with:shape:datatype:name:))*