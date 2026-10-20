# ARConfidenceLevel

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Degrees to which the framework is confident about depth-data accuracy.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
enum ARConfidenceLevel
```

```c
enum ARConfidenceLevel : NSInteger;
```

## Topics

### Levels
- [ARConfidenceLevel.low](./arconfidencelevel/low.md)
  Depth-value accuracy in which the framework is less confident.
- [ARConfidenceLevel.medium](./arconfidencelevel/medium.md)
  Depth-value accuracy in which the framework is moderately confident.
- [ARConfidenceLevel.high](./arconfidencelevel/high.md)
  Depth-value accuracy in which the framework is fairly confident.
### Initializers
- [init?(rawValue: Int)](./arconfidencelevel/init%28rawvalue%29.md)
### Default Implementations
- [Comparable Implementations](./arconfidencelevel/comparable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Comparable](../Swift/comparable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Depth Information
- [var depthMap: CVPixelBuffer](./ardepthdata/depthmap.md)
  The estimated distance from the device to its environment, in meters.
- [var confidenceMap: CVPixelBuffer?](./ardepthdata/confidencemap.md)
  The framework’s confidence in the accuracy of the depth-map data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfidencelevel)*