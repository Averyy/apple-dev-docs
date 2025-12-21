# reversed(alongAxes:)

**Framework**: Core ML  
**Kind**: method

Returns a new tensor with the specified dimensions reversed.

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
func reversed(alongAxes axes: Int...) -> MLTensor
```

#### Return Value

A new tensor with the same shape and scalar type with the specified dimensions reversed.

#### Discussion

For example:

```swift
let x = MLTensor(shape: [4], scalars: [0,  1,  2,  3], scalarType: Float.self)
let y = x.reversed(alongAxes: 0)
// [3, 2, 1, 0]
```

## Parameters

- `axes`: The indices of the dimensions to reverse. Must be in the range  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/reversed(alongaxes:))*