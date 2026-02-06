# longestActivity

**Framework**: DeviceActivity  
**Kind**: property

Access the date interval of the longest activity session during the activity segment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var longestActivity: DateInterval?
```

#### Discussion

This value may be `nil` if the person didn’t use this device during [`dateInterval`](deviceactivitydata/activitysegment/dateinterval.md).

## See Also

- [var totalActivityDuration: TimeInterval](deviceactivitydata/activitysegment/totalactivityduration.md)
  Access the total activity time during the activity segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment/longestactivity)*