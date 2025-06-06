# includesAllActivity

**Framework**: DeviceActivity  
**Kind**: property

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

Use `includesAllActivity` to determine the content of the scheduled event. Evaluates to `true` if [`applications`](deviceactivityevent/applications.md), [`categories`](deviceactivityevent/categories.md), and [`webDomains`](deviceactivityevent/webdomains.md) are empty; otherwise `false`.

## See Also

- [init(applications: Set<ApplicationToken>, categories: Set<ActivityCategoryToken>, webDomains: Set<WebDomainToken>, threshold: DateComponents)](deviceactivityevent/init(applications:categories:webdomains:threshold:).md)
  Creates a new event.
- [DeviceActivityEvent.Name](deviceactivityevent/name.md)
  The unique name of an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/includesallactivity)*