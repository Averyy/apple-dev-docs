# init()

**Framework**: DeviceActivity  
**Kind**: init

Creates an activity center to manage which device activities your application monitors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init()
```

#### Discussion

All instances are equivalent and manage the activities monitored by the application’s extension.

## See Also

- [func startMonitoring(DeviceActivityName, during: DeviceActivitySchedule, events: [DeviceActivityEvent.Name : DeviceActivityEvent]) throws](deviceactivitycenter/startmonitoring(_:during:events:).md)
  Starts monitoring the specified device activity.
- [func stopMonitoring([DeviceActivityName])](deviceactivitycenter/stopmonitoring(_:).md)
  Stops monitoring the specified device activities.
- [var activities: [DeviceActivityName]](deviceactivitycenter/activities.md)
  The activities that the application’s extension currently monitors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/init())*