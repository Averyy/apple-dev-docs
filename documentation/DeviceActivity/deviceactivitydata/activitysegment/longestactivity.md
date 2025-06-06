# longestActivity

**Framework**: DeviceActivity  
**Kind**: property

The date interval of the user’s longest activity session during the activity segment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var longestActivity: DateInterval?
```

#### Discussion

This value may be `nil` if the user was not active on this device during [`dateInterval`](deviceactivitydata/activitysegment/dateinterval.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment/longestactivity)*