# firstPickup

**Framework**: DeviceActivity  
**Kind**: property

The first time the user picked up the device during the activity segment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var firstPickup: Date?
```

#### Discussion

This value may be `nil` if the device was never picked up during [`dateInterval`](deviceactivitydata/activitysegment/dateinterval.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment/firstpickup)*