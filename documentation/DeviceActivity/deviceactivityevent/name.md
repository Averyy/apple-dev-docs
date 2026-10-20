# DeviceActivityEvent.Name

**Framework**: Device Activity  
**Kind**: struct  
**Role**: Structure

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

### Creating an Instance
- [init(rawValue: String)](./name/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [init(String)](./name/init%28_%29.md)
  Creates a new instance with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)

## See Also

### Creating an Event
- [init(applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>, threshold: DateComponents)](./init%28applications,categories,webdomains,threshold%29.md)
  Creates a new event.
- [var includesAllActivity: Bool](./includesallactivity.md)
  A Boolean value that indicates whether the event includes all applications, categories, and web domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/name)*