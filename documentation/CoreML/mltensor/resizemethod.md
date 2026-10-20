# MLTensor.ResizeMethod

**Framework**: Core ML  
**Kind**: enum  
**Role**: Enumeration

A resize algorithm.

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
enum ResizeMethod
```

## Topics

### Resize methods
- [MLTensor.ResizeMethod.bilinear(alignCorners:)](./resizemethod/bilinear%28aligncorners%29.md)
  The bilinear interpolation mode where values are computed using bilinear interpolation of 4 neighboring pixels.
- [MLTensor.ResizeMethod.nearestNeighbor](./resizemethod/nearestneighbor.md)
  The nearest interpolation mode where values are interpolated using the closest neighbor pixel.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Resizing the tensor
- [func resized(to: (newHeight: Int, newWidth: Int), method: MLTensor.ResizeMethod) -> MLTensor](./resized%28to,method%29.md)
  Resize the tensor’s spatial dimensions to size using the specified method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/resizemethod)*