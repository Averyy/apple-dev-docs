# stopMonitoring(_:)

**Framework**: DeviceActivity  
**Kind**: method

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

- `activities`: The names of the activities. If the array is empty or no   are explicitly specified,   this method stops monitoring all activities.

## See Also

- [init()](deviceactivitycenter/init.md)
  Creates an activity center to manage which device activities your application monitors.
- [func startMonitoring(DeviceActivityName, during: DeviceActivitySchedule, events: [DeviceActivityEvent.Name : DeviceActivityEvent]) throws](deviceactivitycenter/startmonitoring(_:during:events:).md)
  Starts monitoring the specified device activity.
- [var activities: [DeviceActivityName]](deviceactivitycenter/activities.md)
  The activities that the application’s extension currently monitors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/stopmonitoring(_:))*