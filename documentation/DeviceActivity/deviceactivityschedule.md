# DeviceActivitySchedule

**Framework**: DeviceActivity  
**Kind**: struct

A calendar-based schedule for when to monitor a device’s activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct DeviceActivitySchedule
```

#### Overview

Create a new schedule using `DateComponents` that allows your app to monitor the person’s device activity during a period of time. You can set a schedule for your app to monitor on a regularly occuring basis. You can create a warning time that the system uses to provide your app extension with callbacks whenever a schedule is about to start or end, or when an event is close to reaching its threshold.

## Topics

### Creating a Schedule
- [init(intervalStart: DateComponents, intervalEnd: DateComponents, repeats: Bool, warningTime: DateComponents?)](deviceactivityschedule/init(intervalstart:intervalend:repeats:warningtime:).md)
  Creates a new schedule.
- [var intervalEnd: DateComponents](deviceactivityschedule/intervalend.md)
  The date components that represent the end time for a schedule’s interval.
- [var intervalStart: DateComponents](deviceactivityschedule/intervalstart.md)
  The date components that represent the start time for a schedule’s interval.
- [var nextInterval: DateInterval?](deviceactivityschedule/nextinterval.md)
  The schedule’s next interval or the current interval if one is ongoing.
- [var repeats: Bool](deviceactivityschedule/repeats.md)
  A Boolean value that indicates whether the schedule recurs.
- [var warningTime: DateComponents?](deviceactivityschedule/warningtime.md)
  Optional components that generate a warning prior to regularly scheduled events.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct DeviceActivityEvent](deviceactivityevent.md)
  An event that represents an application, category, or website activity.
- [struct DeviceActivityName](deviceactivityname.md)
  The unique name of an activity.
- [struct DeviceActivityCenter](deviceactivitycenter.md)
  A class that enables an application’s extension to start monitoring scheduled device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityschedule)*