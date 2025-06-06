# expandingShape(at:)

**Framework**: Core ML  
**Kind**: method

Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func expandingShape(at axes: Int...) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor(shape: [2], scalars: [1, 2], scalarType: Float.self)
let y = x.expandingShape(at: 0)
y.shape // is [1, 2]
```

## Parameters

- `axes`: The axes at which to expand the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/expandingshape(at:)-1daz8)*