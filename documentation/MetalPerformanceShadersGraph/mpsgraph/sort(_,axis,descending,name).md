# sort(_:axis:descending:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Sorts the elements of the input tensor along the specified axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func sort(_ tensor: MPSGraphTensor, axis: Int, descending: Bool, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

## Parameters

- `tensor`: The input tensor
- `axis`: The tensor dimension over which you sort the tensor
- `descending`: If true, reverse the sort direction
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/sort(_:axis:descending:name:))*