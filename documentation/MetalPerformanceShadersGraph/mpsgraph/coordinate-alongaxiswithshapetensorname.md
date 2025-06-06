# coordinate(alongAxis:withShapeTensor:name:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Creates a get-coordindate operation and returns the result tensor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 12.3+
- tvOS 15.4+
- visionOS 1.0+

## Declaration

```swift
func coordinate(alongAxis axis: Int, withShapeTensor shapeTensor: MPSGraphTensor, name: String?) -> MPSGraphTensor
```

#### Return Value

A valid MPSGraphTensor object.

#### Discussion

See [`coordinate(alongAxis:withShape:name:)`](mpsgraph/coordinate(alongaxis:withshape:name:).md).

## Parameters

- `axis`: The coordinate axis an element’s value is set to. Negative values wrap around.
- `shapeTensor`: A rank-1 tensor of type   or   that defines the shape of the result tensor.
- `name`: The name for the operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraph/coordinate(alongaxis:withshapetensor:name:))*