# CMHighFrequencyHeartRateDataConfidence

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum CMHighFrequencyHeartRateDataConfidence : NSInteger;
```

## Topics

### Levels of confidence
- [CMHighFrequencyHeartRateDataConfidence.low](./cmhighfrequencyheartratedataconfidence/low.md)
  A low level of confidence in the heart rate data.
- [CMHighFrequencyHeartRateDataConfidence.medium](./cmhighfrequencyheartratedataconfidence/medium.md)
  A medium level of confidence in the heart rate data.
- [CMHighFrequencyHeartRateDataConfidence.high](./cmhighfrequencyheartratedataconfidence/high.md)
  A high level of confidence in the heart rate data.
- [CMHighFrequencyHeartRateDataConfidence.highest](./cmhighfrequencyheartratedataconfidence/highest.md)
  The highest level of confidence in the heart rate data.
### Initializers
- [init?(rawValue: Int)](./cmhighfrequencyheartratedataconfidence/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing heart rate data
- [var heartRate: Double](./cmhighfrequencyheartratedata/heartrate.md)
  The heart rate value in units of beats per minute (BPM).
- [var confidence: CMHighFrequencyHeartRateDataConfidence](./cmhighfrequencyheartratedata/confidence.md)
  The confidence level of the heart rate value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedataconfidence)*