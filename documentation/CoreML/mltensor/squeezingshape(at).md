# squeezingShape(at:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Removes the specified dimensions of size 1 from the shape of the tensor.

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
func squeezingShape(at axes: Int...) -> MLTensor
```

**Other overloads**:

```swift
func squeezingShape(at axes: [Int]) -> MLTensor
```

#### Discussion

For example:

```swift
let x = MLTensor(shape: [1, 2, 1], scalars: [1, 2], scalarType: Float.self)
let y = x.squeezingShape(at: 0)
y.shape // is [2, 1]
```

## Parameters

- `axes`: The axes to remove if the size is `1`.

## See Also

### Removing dimensions from the shape of the tensor
- [func squeezingShape() -> MLTensor](./squeezingshape%28%29.md)
  Removes all dimensions of size 1 from the shape of the tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/squeezingshape(at:))*