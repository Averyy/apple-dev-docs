# resized(to:method:)

**Framework**: Core ML  
**Kind**: method

Resize the tensor’s spatial dimensions to size using the specified method.

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
func resized(to size: (newHeight: Int, newWidth: Int), method: MLTensor.ResizeMethod = .nearestNeighbor) -> MLTensor
```

#### Discussion

For example:

```swift
let image = MLTensor(shape: [1, 1, 2, 2], scalars: [
    1, 0,
    0, 1
], scalarType: Float.self)
let resizedImage = image.resized(to: (4, 4), method: .nearest)
// [[[[1, 1, 0, 0],
//    [1, 1, 0, 0],
//    [0, 0, 1, 1],
//    [0, 0, 1, 1]]]]
```

The tensor must be either a 4-dimensional float tensor of shape `[batch, channels, height, width]` or 3-dimensional float tensor of shape `[channel, height, width]`.

## Parameters

- `size`: The new size for the spatial dimensions of the tensor. The size must be positive.
- `method`: The resize method. The default value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/resized(to:method:))*