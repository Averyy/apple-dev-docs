# DeviceActivityData.ActivitySegment

**Framework**: DeviceActivity  
**Kind**: struct

Activity data for a specific time interval.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct ActivitySegment
```

#### Overview

This type contains all of the activity details for a particular person on a particular device during [`dateInterval`](deviceactivitydata/activitysegment/dateinterval.md).

## Topics

### Defining the segment
- [var dateInterval: DateInterval](deviceactivitydata/activitysegment/dateinterval.md)
  Access the date interval of the activity segment.
### Measuring activity
- [var totalActivityDuration: TimeInterval](deviceactivitydata/activitysegment/totalactivityduration.md)
  Access the total activity time during the activity segment.
- [var longestActivity: DateInterval?](deviceactivitydata/activitysegment/longestactivity.md)
  Access the date interval of the longest activity session during the activity segment.
### Tracking device usage
- [var firstPickup: Date?](deviceactivitydata/activitysegment/firstpickup.md)
  Access the first time the person picked up the device during the activity segment.
- [var totalPickupsWithoutApplicationActivity: Int](deviceactivitydata/activitysegment/totalpickupswithoutapplicationactivity.md)
  Access the number of device pickups without application use.
### Accessing categorized activity
- [var categories: DeviceActivityResults<DeviceActivityData.CategoryActivity>](deviceactivitydata/activitysegment/categories.md)
  Access the categorized device activity during the activity segment.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [var activitySegments: DeviceActivityResults<DeviceActivityData.ActivitySegment>](deviceactivitydata/activitysegments.md)
  Access the activity divided into segments.
- [var segmentInterval: DeviceActivityFilter.SegmentInterval](deviceactivitydata/segmentinterval.md)
  Access the segment interval of each activity segment.
- [var lastUpdatedDate: Date](deviceactivitydata/lastupdateddate.md)
  Access the date when the system last updated the data for this device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegment)*