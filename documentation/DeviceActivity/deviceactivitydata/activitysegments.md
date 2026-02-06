# activitySegments

**Framework**: DeviceActivity  
**Kind**: property

Access the activity divided into segments.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var activitySegments: DeviceActivityResults<DeviceActivityData.ActivitySegment> { get }
```

#### Discussion

The [`segmentInterval`](deviceactivitydata/segmentinterval.md) that your app requests via a [`DeviceActivityFilter`](deviceactivityfilter.md) determines the length of each activity segment.

## See Also

- [var segmentInterval: DeviceActivityFilter.SegmentInterval](deviceactivitydata/segmentinterval.md)
  Access the segment interval of each activity segment.
- [var lastUpdatedDate: Date](deviceactivitydata/lastupdateddate.md)
  Access the date when the system last updated the data for this device.
- [DeviceActivityData.ActivitySegment](deviceactivitydata/activitysegment.md)
  Activity data for a specific time interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegments)*