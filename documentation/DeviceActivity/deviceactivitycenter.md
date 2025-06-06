# DeviceActivityCenter

**Framework**: DeviceActivity  
**Kind**: struct

A class that enables an application’s extension to start monitoring scheduled device activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct DeviceActivityCenter
```

#### Overview

Activity begins when someone first uses a device within the scheduled time interval and ends when someone first uses the device outside of the interval. The system only invokes the [`intervalDidStart(for:)`](deviceactivitymonitor/intervaldidstart(for:).md) and [`intervalDidEnd(for:)`](deviceactivitymonitor/intervaldidend(for:).md) when the device is in use. Likewise, the system invokes the [`eventDidReachThreshold(_:activity:)`](deviceactivitymonitor/eventdidreachthreshold(_:activity:).md) function when an event reaches its threshold.

## Topics

### Monitoring Device Activities
- [init()](deviceactivitycenter/init.md)
  Creates an activity center to manage which device activities your application monitors.
- [func startMonitoring(DeviceActivityName, during: DeviceActivitySchedule, events: [DeviceActivityEvent.Name : DeviceActivityEvent]) throws](deviceactivitycenter/startmonitoring(_:during:events:).md)
  Starts monitoring the specified device activity.
- [func stopMonitoring([DeviceActivityName])](deviceactivitycenter/stopmonitoring(_:).md)
  Stops monitoring the specified device activities.
- [var activities: [DeviceActivityName]](deviceactivitycenter/activities.md)
  The activities that the application’s extension currently monitors.
### Getting the Events and Schedules
- [func events(for: DeviceActivityName) -> [DeviceActivityEvent.Name : DeviceActivityEvent]](deviceactivitycenter/events(for:).md)
  Fetches the events of a device activity.
- [func schedule(for: DeviceActivityName) -> DeviceActivitySchedule?](deviceactivitycenter/schedule(for:).md)
  Fetches the schedule of a device activity.
### Enumerations
- [DeviceActivityCenter.MonitoringError](deviceactivitycenter/monitoringerror.md)
  Errors that may occur when starting to monitor an activity.

## See Also

- [struct DeviceActivityEvent](deviceactivityevent.md)
  An event that represents an application, category, or website activity.
- [struct DeviceActivityName](deviceactivityname.md)
  The unique name of an activity.
- [struct DeviceActivitySchedule](deviceactivityschedule.md)
  A calendar-based schedule for when to monitor a device’s activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivitycenter)*