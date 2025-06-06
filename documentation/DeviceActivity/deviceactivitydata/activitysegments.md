# activitySegments

**Framework**: DeviceActivity  
**Kind**: property

The activity of the user divided into segments.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var activitySegments: DeviceActivityResults<DeviceActivityData.ActivitySegment> { get }
```

#### Discussion

The length of each activity segment is dependent on the [`segmentInterval`](deviceactivitydata/segmentinterval.md) that your app requests via a [`DeviceActivityFilter`](deviceactivityfilter.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitydata/activitysegments)*