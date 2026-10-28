# firstPickup

**Framework**: Device Activity  
**Kind**: property  
**Role**: Instance Property

Access the first time the person picked up the device during the activity segment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var firstPickup: Date?
```

## Discussion

This value may be `nil` if the person never picked up the device during [`dateInterval`](./dateinterval.md).

## See Also

### Tracking device usage
- [var totalPickupsWithoutApplicationActivity: Int](./totalpickupswithoutapplicationactivity.md)
  Access the number of device pickups without application use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment/firstpickup)*