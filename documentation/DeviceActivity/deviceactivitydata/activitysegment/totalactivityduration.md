# totalActivityDuration

**Framework**: Device Activity  
**Kind**: property  
**Role**: Instance Property

Access the total activity time during the activity segment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var totalActivityDuration: TimeInterval
```

#### Discussion

This value represents the total amount of time the device’s screen remained on during [`dateInterval`](./dateinterval.md).

## See Also

### Measuring activity
- [var longestActivity: DateInterval?](./longestactivity.md)
  Access the date interval of the longest activity session during the activity segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment/totalactivityduration)*