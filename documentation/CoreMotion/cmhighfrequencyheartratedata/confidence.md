# confidence

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The confidence level of the heart rate value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- watchOS 10.0+

## Declaration

```swift
var confidence: CMHighFrequencyHeartRateDataConfidence { get }
```

```objc
@property (nonatomic, readonly) CMHighFrequencyHeartRateDataConfidence confidence;
```

## See Also

### Accessing heart rate data
- [var heartRate: Double](./heartrate.md)
  The heart rate value in units of beats per minute (BPM).
- [enum CMHighFrequencyHeartRateDataConfidence](../cmhighfrequencyheartratedataconfidence.md)
  The level of confidence in the accuracy of the heart rate data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmhighfrequencyheartratedata/confidence)*