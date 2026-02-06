# DeviceActivityData

**Framework**: DeviceActivity  
**Kind**: struct

Activity data for a person on a specific device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct DeviceActivityData
```

## Topics

### Accessing device and user information
- [var user: DeviceActivityData.User](deviceactivitydata/user-swift.property.md)
  Access the person associated with the activity report.
- [var device: DeviceActivityData.Device](deviceactivitydata/device-swift.property.md)
  Access the device associated with the activity report.
- [DeviceActivityData.User](deviceactivitydata/user-swift.struct.md)
  Information about a person associated with an activity report.
- [DeviceActivityData.Device](deviceactivitydata/device-swift.struct.md)
  Device information for activity reporting.
### Managing activity data
- [var activitySegments: DeviceActivityResults<DeviceActivityData.ActivitySegment>](deviceactivitydata/activitysegments.md)
  Access the activity divided into segments.
- [var segmentInterval: DeviceActivityFilter.SegmentInterval](deviceactivitydata/segmentinterval.md)
  Access the segment interval of each activity segment.
- [var lastUpdatedDate: Date](deviceactivitydata/lastupdateddate.md)
  Access the date when the system last updated the data for this device.
- [DeviceActivityData.ActivitySegment](deviceactivitydata/activitysegment.md)
  Activity data for a specific time interval.
### Organizing activity by type
- [DeviceActivityData.ApplicationActivity](deviceactivitydata/applicationactivity.md)
  Activity data for an application.
- [DeviceActivityData.CategoryActivity](deviceactivitydata/categoryactivity.md)
  Categorized representation of application and web domain activity.
- [DeviceActivityData.WebDomainActivity](deviceactivitydata/webdomainactivity.md)
  Activity data for a web domain.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct DeviceActivityFilter](deviceactivityfilter.md)
  A type that filters the device activity data to include in a report.
- [struct DeviceActivityResults](deviceactivityresults.md)
  An asynchronous sequence of filtered device activity results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata)*