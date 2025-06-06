# CMHighFrequencyHeartRateDataConfidence

**Framework**: Core Motion  
**Kind**: enum

The level of confidence in the accuracy of the heart rate data.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
enum CMHighFrequencyHeartRateDataConfidence
```

## Topics

### Levels of confidence
- [CMHighFrequencyHeartRateDataConfidence.low](cmhighfrequencyheartratedataconfidence/low.md)
  A low level of confidence in the heart rate data.
- [CMHighFrequencyHeartRateDataConfidence.medium](cmhighfrequencyheartratedataconfidence/medium.md)
  A medium level of confidence in the heart rate data.
- [CMHighFrequencyHeartRateDataConfidence.high](cmhighfrequencyheartratedataconfidence/high.md)
  A high level of confidence in the heart rate data.
- [CMHighFrequencyHeartRateDataConfidence.highest](cmhighfrequencyheartratedataconfidence/highest.md)
  The highest level of confidence in the heart rate data.
### Initializers
- [init?(rawValue: Int)](cmhighfrequencyheartratedataconfidence/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var heartRate: Double](cmhighfrequencyheartratedata/heartrate.md)
  The heart rate value in units of beats per minute (BPM).
- [var confidence: CMHighFrequencyHeartRateDataConfidence](cmhighfrequencyheartratedata/confidence.md)
  The confidence level of the heart rate value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence)*