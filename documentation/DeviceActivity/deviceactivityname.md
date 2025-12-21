# DeviceActivityName

**Framework**: DeviceActivity  
**Kind**: struct

The unique name of an activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct DeviceActivityName
```

#### Overview

Use `DeviceActivityName` to associate an activity with some of your application’s data. It’s not possible to have multiple activities with the same name. Monitoring a second activity with the same name as a previous activity overwrites the schedule for the first one.

## Topics

### Creating an Instance
- [init(rawValue: String)](deviceactivityname/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init(String)](deviceactivityname/init(_:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [struct DeviceActivityEvent](deviceactivityevent.md)
  An event that represents an application, category, or website activity.
- [struct DeviceActivitySchedule](deviceactivityschedule.md)
  A calendar-based schedule for when to monitor a device’s activity.
- [struct DeviceActivityCenter](deviceactivitycenter.md)
  A class that enables an application’s extension to start monitoring scheduled device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityname)*