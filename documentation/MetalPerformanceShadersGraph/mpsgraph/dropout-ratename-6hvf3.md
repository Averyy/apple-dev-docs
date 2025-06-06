# dropout(_:rate:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a dropout operation and returns the result

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func dropout(_ tensor: MPSGraphTensor, rate: Double, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object

#### Discussion

Removes values in the `tensor` with a percentage chance equal to `rate`. Removed values are set to 0

## Parameters

- `tensor`: Input tensor
- `rate`: The rate of values to be set to 0
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/dropout(_:rate:name:)-6hvf3)*