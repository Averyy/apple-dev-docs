# MLTensor.ResizeMethod

**Framework**: Core ML  
**Kind**: enum

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
- [MLTensor.ResizeMethod.bilinear(alignCorners:)](mltensor/resizemethod/bilinear(aligncorners:).md)
  The bilinear interpolation mode where values are computed using bilinear interpolation of 4 neighboring pixels.
- [MLTensor.ResizeMethod.nearestNeighbor](mltensor/resizemethod/nearestneighbor.md)
  The nearest interpolation mode where values are interpolated using the closest neighbor pixel.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func resized(to: (newHeight: Int, newWidth: Int), method: MLTensor.ResizeMethod) -> MLTensor](mltensor/resized(to:method:).md)
  Resize the tensor’s spatial dimensions to size using the specified method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/resizemethod)*