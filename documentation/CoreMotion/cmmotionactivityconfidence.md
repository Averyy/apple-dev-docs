# CMMotionActivityConfidence

**Framework**: Core Motion  
**Kind**: enum

The confidence that the motion data is accurate.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CMMotionActivityConfidence
```

## Topics

### Constants
- [CMMotionActivityConfidence.low](cmmotionactivityconfidence/low.md)
  Confidence is low.
- [CMMotionActivityConfidence.medium](cmmotionactivityconfidence/medium.md)
  Confidence is good.
- [CMMotionActivityConfidence.high](cmmotionactivityconfidence/high.md)
  Confidence is high.
### Initializers
- [init?(rawValue: Int)](cmmotionactivityconfidence/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var startDate: Date](cmmotionactivity/startdate.md)
  The time at which the change in motion occurred.
- [var confidence: CMMotionActivityConfidence](cmmotionactivity/confidence.md)
  The confidence in the assessment of the motion type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionactivityconfidence)*