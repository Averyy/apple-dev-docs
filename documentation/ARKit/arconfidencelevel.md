# ARConfidenceLevel

**Framework**: ARKit  
**Kind**: enum

Degrees to which the framework is confident about depth-data accuracy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

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
### Default Implementations
- [Comparable Implementations](arconfidencelevel/comparable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Comparable](../swift/comparable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var depthMap: CVPixelBuffer](ardepthdata/depthmap.md)
  The estimated distance from the device to its environment, in meters.
- [var confidenceMap: CVPixelBuffer?](ardepthdata/confidencemap.md)
  The framework’s confidence in the accuracy of the depth-map data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfidencelevel)*