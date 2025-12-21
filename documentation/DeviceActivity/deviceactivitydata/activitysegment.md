# DeviceActivityData.ActivitySegment

**Framework**: DeviceActivity  
**Kind**: struct

Represents the user’s activity during a particular date interval.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct ActivitySegment
```

#### Overview

This type contains all of the activity details for a particular user on a particular device during [`dateInterval`](deviceactivitydata/activitysegment/dateinterval.md).

## Topics

### Instance Properties
- [var categories: DeviceActivityResults<DeviceActivityData.CategoryActivity>](deviceactivitydata/activitysegment/categories.md)
  The user’s categorized device activity during the activity segment.
- [var dateInterval: DateInterval](deviceactivitydata/activitysegment/dateinterval.md)
  The date interval of the activity segment.
- [var firstPickup: Date?](deviceactivitydata/activitysegment/firstpickup.md)
  The first time the user picked up the device during the activity segment.
- [var longestActivity: DateInterval?](deviceactivitydata/activitysegment/longestactivity.md)
  The date interval of the user’s longest activity session during the activity segment.
- [var totalActivityDuration: TimeInterval](deviceactivitydata/activitysegment/totalactivityduration.md)
  The total activity during the activity segment.
- [var totalPickupsWithoutApplicationActivity: Int](deviceactivitydata/activitysegment/totalpickupswithoutapplicationactivity.md)
  The number of times the user picked up the device but did not use any applications.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment)*