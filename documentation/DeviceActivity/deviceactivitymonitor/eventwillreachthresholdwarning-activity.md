# eventWillReachThresholdWarning(_:activity:)

**Framework**: DeviceActivity  
**Kind**: method

Warns your app that an activity is about to reach its threshold.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func eventWillReachThresholdWarning(_ event: DeviceActivityEvent.Name, activity: DeviceActivityName)
```

#### Discussion

When an activity is about to reach its threshold, `eventWillReachThresholdWarning` warns your app extension of the concluding threshold limit.

## Parameters

- `event`: The name of the event.
- `activity`: The name of the activity.

## See Also

- [func eventDidReachThreshold(DeviceActivityEvent.Name, activity: DeviceActivityName)](deviceactivitymonitor/eventdidreachthreshold(_:activity:).md)
  Indicates that the activity reached its threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor/eventwillreachthresholdwarning(_:activity:))*