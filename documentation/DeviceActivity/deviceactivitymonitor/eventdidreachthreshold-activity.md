# eventDidReachThreshold(_:activity:)

**Framework**: DeviceActivity  
**Kind**: method

Indicates that the activity reached its threshold.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func eventDidReachThreshold(_ event: DeviceActivityEvent.Name, activity: DeviceActivityName)
```

#### Discussion

The system invokes this method when use of the `activity` reaches its threshold.

## Parameters

- `event`: The name of the event.
- `activity`: The name of the activity.

## See Also

- [func eventWillReachThresholdWarning(DeviceActivityEvent.Name, activity: DeviceActivityName)](deviceactivitymonitor/eventwillreachthresholdwarning(_:activity:).md)
  Warns your app that an activity is about to reach its threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitymonitor/eventdidreachthreshold(_:activity:))*