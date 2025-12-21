# DeviceActivityData

**Framework**: DeviceActivity  
**Kind**: struct

Represents the activity of a [`DeviceActivityData.User`](deviceactivitydata/user-swift.struct.md) on a particular [`DeviceActivityData.Device`](deviceactivitydata/device-swift.struct.md).

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct DeviceActivityData
```

## Topics

### Structures
- [DeviceActivityData.ActivitySegment](deviceactivitydata/activitysegment.md)
  Represents the user’s activity during a particular date interval.
- [DeviceActivityData.ApplicationActivity](deviceactivitydata/applicationactivity.md)
- [DeviceActivityData.CategoryActivity](deviceactivitydata/categoryactivity.md)
  A categorized representation of a user’s application and web domain activity.
- [DeviceActivityData.Device](deviceactivitydata/device-swift.struct.md)
  A device for which to report activity data.
- [DeviceActivityData.User](deviceactivitydata/user-swift.struct.md)
- [DeviceActivityData.WebDomainActivity](deviceactivitydata/webdomainactivity.md)
### Instance Properties
- [var activitySegments: DeviceActivityResults<DeviceActivityData.ActivitySegment>](deviceactivitydata/activitysegments.md)
  The activity of the user divided into segments.
- [var device: DeviceActivityData.Device](deviceactivitydata/device-swift.property.md)
  The device associated with the activity report.
- [var lastUpdatedDate: Date](deviceactivitydata/lastupdateddate.md)
  The date when the system last updated the data for this device.
- [var segmentInterval: DeviceActivityFilter.SegmentInterval](deviceactivitydata/segmentinterval.md)
  The segment interval of each [`DeviceActivityData.ActivitySegment`](deviceactivitydata/activitysegment.md) in [`activitySegments`](deviceactivitydata/activitysegments.md).
- [var user: DeviceActivityData.User](deviceactivitydata/user-swift.property.md)
  The user associated with the activity report.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata)*