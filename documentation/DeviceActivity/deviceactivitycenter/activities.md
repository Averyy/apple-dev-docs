# activities

**Framework**: DeviceActivity  
**Kind**: property

The activities that the application’s extension currently monitors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var activities: [DeviceActivityName] { get }
```

## See Also

- [init()](deviceactivitycenter/init.md)
  Creates an activity center to manage which device activities your application monitors.
- [func startMonitoring(DeviceActivityName, during: DeviceActivitySchedule, events: [DeviceActivityEvent.Name : DeviceActivityEvent]) throws](deviceactivitycenter/startmonitoring(_:during:events:).md)
  Starts monitoring the specified device activity.
- [func stopMonitoring([DeviceActivityName])](deviceactivitycenter/stopmonitoring(_:).md)
  Stops monitoring the specified device activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/activities)*