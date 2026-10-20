# activities

**Framework**: Device Activity  
**Kind**: property  
**Role**: Instance Property

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

### Monitoring Device Activities
- [init()](./init%28%29.md)
  Creates an activity center to manage which device activities your application monitors.
- [func startMonitoring(DeviceActivityName, during: DeviceActivitySchedule, events: [DeviceActivityEvent.Name : DeviceActivityEvent]) throws](./startmonitoring%28_,during,events%29.md)
  Starts monitoring the specified device activity.
- [func stopMonitoring([DeviceActivityName])](./stopmonitoring%28_%29.md)
  Stops monitoring the specified device activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter/activities)*