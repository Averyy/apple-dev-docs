# firstPickup

**Framework**: Device Activity  
**Kind**: property

Access the first time the person picked up the device during the activity segment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var firstPickup: Date?
```

#### Discussion

This value may be `nil` if the person never picked up the device during [`dateInterval`](deviceactivitydata/activitysegment/dateinterval.md).

## See Also

- [var totalPickupsWithoutApplicationActivity: Int](deviceactivitydata/activitysegment/totalpickupswithoutapplicationactivity.md)
  Access the number of device pickups without application use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment/firstpickup)*