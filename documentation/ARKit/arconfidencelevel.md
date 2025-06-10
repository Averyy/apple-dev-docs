# ARConfidenceLevel

**Framework**: ARKit  
**Kind**: enum

Degrees to which the framework is confident about depth-data accuracy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
enum ARConfidenceLevel
```

## Topics

### Levels
- [ARConfidenceLevel.low](arconfidencelevel/low.md)
  Depth-value accuracy in which the framework is less confident.
- [ARConfidenceLevel.medium](arconfidencelevel/medium.md)
  Depth-value accuracy in which the framework is moderately confident.
- [ARConfidenceLevel.high](arconfidencelevel/high.md)
  Depth-value accuracy in which the framework is fairly confident.
### Initializers
- [init?(rawValue: Int)](arconfidencelevel/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var depthMap: CVPixelBuffer](ardepthdata/depthmap.md)
  The estimated distance from the device to its environment, in meters.
- [var confidenceMap: CVPixelBuffer?](ardepthdata/confidencemap.md)
  The framework’s confidence in the accuracy of the depth-map data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfidencelevel)*