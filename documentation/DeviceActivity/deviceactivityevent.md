# DeviceActivityEvent

**Framework**: DeviceActivity  
**Kind**: struct

An event that represents an application, category, or website activity.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct DeviceActivityEvent
```

#### Overview

Device activity is the amount of time an application, category, or web domain is frontmost on the screen and accumulates based on the time zone of the scheduled start date. Web domain activity includes domains visited in Safari or any third-party browser that contributes web usage via a `STWebpageController`.

## Topics

### Creating an Event
- [init(applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>, threshold: DateComponents)](deviceactivityevent/init(applications:categories:webdomains:threshold:).md)
  Creates a new event.
- [DeviceActivityEvent.Name](deviceactivityevent/name.md)
  The unique name of an event.
- [var includesAllActivity: Bool](deviceactivityevent/includesallactivity.md)
  A Boolean value that indicates whether the event includes all applications, categories, and web domains.
### Including Objects in an Event
- [var applications: Set<ApplicationToken>](deviceactivityevent/applications.md)
  The applications that the event includes.
- [var categories: Set<ActivityCategoryToken>](deviceactivityevent/categories.md)
  The categories that the event includes.
- [var webDomains: Set<WebDomainToken>](deviceactivityevent/webdomains.md)
  The web domains that the event includes.
- [var threshold: DateComponents](deviceactivityevent/threshold.md)
  The amount of time to monitor the provided applications, categories, and web domains.
### Comparing Events and Schedules
- [static func != (Self, Self) -> Bool](deviceactivityevent/!=(_:_:).md)
  Returns a Boolean value that indicates whether two values aren’t equal.
- [static func == (DeviceActivityEvent, DeviceActivityEvent) -> Bool](deviceactivityevent/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>, threshold: DateComponents, includesPastActivity: Bool)](deviceactivityevent/init(applications:categories:webdomains:threshold:includespastactivity:).md)
  Creates a new event.
### Instance Properties
- [var includesPastActivity: Bool](deviceactivityevent/includespastactivity.md)
  Whether the system takes into account the person’s device activity before your app starts monitoring the event.
### Default Implementations
- [Equatable Implementations](deviceactivityevent/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct DeviceActivityName](deviceactivityname.md)
  The unique name of an activity.
- [struct DeviceActivitySchedule](deviceactivityschedule.md)
  A calendar-based schedule for when to monitor a device’s activity.
- [struct DeviceActivityCenter](deviceactivitycenter.md)
  A class that enables an application’s extension to start monitoring scheduled device activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent)*