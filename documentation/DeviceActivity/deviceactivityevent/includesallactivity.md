# includesAllActivity

**Framework**: Device Activity  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the event includes all applications, categories, and web domains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var includesAllActivity: Bool { get }
```

#### Discussion

Use `includesAllActivity` to determine the content of the scheduled event. Evaluates to `true` if [`applications`](./applications.md), [`categories`](./categories.md), and [`webDomains`](./webdomains.md) are empty; otherwise `false`.

## See Also

### Creating an Event
- [init(applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>, threshold: DateComponents)](./init%28applications,categories,webdomains,threshold%29.md)
  Creates a new event.
- [DeviceActivityEvent.Name](./name.md)
  The unique name of an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/includesallactivity)*