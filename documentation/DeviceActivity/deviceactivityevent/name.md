# DeviceActivityEvent.Name

**Framework**: DeviceActivity  
**Kind**: struct

The unique name of an event.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct Name
```

#### Overview

`DeviceActivityEvent.Name` allows applications to associate an event with some of their own data.

## Topics

### Accessing the Raw Value
- [init(rawValue: String)](deviceactivityevent/name/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [init(String)](deviceactivityevent/name/init(_:).md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [init(applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>, threshold: DateComponents)](deviceactivityevent/init(applications:categories:webdomains:threshold:).md)
  Creates a new event.
- [var includesAllActivity: Bool](deviceactivityevent/includesallactivity.md)
  A Boolean value that indicates whether the event includes all applications, categories, and web domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/name)*