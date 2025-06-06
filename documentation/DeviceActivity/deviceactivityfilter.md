# DeviceActivityFilter

**Framework**: DeviceActivity  
**Kind**: struct

A type that filters the device activity data to include in a report.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct DeviceActivityFilter
```

#### Overview

Your app can choose to filter device activity data for a specific date interval, filter by user and device, as well as specify a subset of applications, categories, and web domains to include in a report.

## Topics

### Structures
- [DeviceActivityFilter.Devices](deviceactivityfilter/devices-swift.struct.md)
  A type your app uses to indiciate which devices to include in a device activity report.
- [DeviceActivityFilter.Users](deviceactivityfilter/users-swift.struct.md)
  A type your app uses to indicate which users to include in a device activity report.
### Operators
- [static func == (DeviceActivityFilter, DeviceActivityFilter) -> Bool](deviceactivityfilter/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(segment: DeviceActivityFilter.SegmentInterval, devices: DeviceActivityFilter.Devices?, applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>)](deviceactivityfilter/init(segment:devices:applications:categories:webdomains:).md)
  Creates a new filter for the current user.
- [init(segment: DeviceActivityFilter.SegmentInterval, users: DeviceActivityFilter.Users, devices: DeviceActivityFilter.Devices, applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>)](deviceactivityfilter/init(segment:users:devices:applications:categories:webdomains:).md)
  Creates a new filter for the specified users and devices.
### Instance Properties
- [var applications: Set<ApplicationToken>](deviceactivityfilter/applications.md)
  An optional set of applications to include in a report.
- [var categories: Set<ActivityCategoryToken>](deviceactivityfilter/categories.md)
  An optional set of categories to include in a report.
- [let devices: DeviceActivityFilter.Devices?](deviceactivityfilter/devices-swift.property.md)
  The devices to include in a report.
- [var segmentInterval: DeviceActivityFilter.SegmentInterval](deviceactivityfilter/segmentinterval-swift.property.md)
  The interval at which the system subdivides the report’s device activity data during a specified date interval.
- [let users: DeviceActivityFilter.Users?](deviceactivityfilter/users-swift.property.md)
  The users to include in a report.
- [var webDomains: Set<WebDomainToken>](deviceactivityfilter/webdomains.md)
  An optional set of web domains to include in a report.
### Enumerations
- [DeviceActivityFilter.SegmentInterval](deviceactivityfilter/segmentinterval-swift.enum.md)
  A type indicating the interval at which the system subdivides device activity data within a specified date interval.
### Default Implementations
- [Equatable Implementations](deviceactivityfilter/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityfilter)*