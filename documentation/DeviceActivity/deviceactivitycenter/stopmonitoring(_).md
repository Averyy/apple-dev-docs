# stopMonitoring(_:)

**Framework**: Device Activity  
**Kind**: method  
**Role**: Instance Method

Stops monitoring the specified device activities.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
func stopMonitoring(_ activities: [DeviceActivityName] = [])
```

#### Discussion

This method ignores names that don’t correspond to monitored activities.

## Parameters

- `activities`: The names of the activities. If the array is empty or no `activities` are explicitly specified, this method stops monitoring all activities.

## See Also

### Monitoring Device Activities
- [init()](./init%28%29.md)
  Creates an activity center to manage which device activities your application monitors.
- [func startMonitoring(DeviceActivityName, during: DeviceActivitySchedule, events: [DeviceActivityEvent.Name : DeviceActivityEvent]) throws](./startmonitoring%28_,during,events%29.md)
  Starts monitoring the specified device activity.
- [var activities: [DeviceActivityName]](./activities.md)
  The activities that the application’s extension currently monitors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/stopmonitoring(_:))*