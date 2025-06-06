# init(applications:categories:webDomains:threshold:)

**Framework**: DeviceActivity  
**Kind**: init

Creates a new event.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init(applications: Set<ApplicationToken> = [], categories: Set<ActivityCategoryToken> = [], webDomains: Set<WebDomainToken> = [], threshold: DateComponents)
```

#### Discussion

An application’s extension receives a callback once the combination of specified [`applications`](deviceactivityevent/applications.md), [`categories`](deviceactivityevent/categories.md), and [`webDomains`](deviceactivityevent/webdomains.md) have been in use longer than the event’s threshold within the activity’s scheduled interval. If your app didn’t specify any `applications`, `categories`, or `webDomains`, the event includes all `applications`, `categories`, and `web domains`.

> ❗ **Important**: When your app calls [`startMonitoring(_:during:events:)`](deviceactivitycenter/startmonitoring(_:during:events:).md) and the event’s schedule is active, the system will only consider the person’s device activity when it starts monitoring the event.

When your app calls [`startMonitoring(_:during:events:)`](deviceactivitycenter/startmonitoring(_:during:events:).md) and the event’s schedule is active, the system will only consider the person’s device activity when it starts monitoring the event.

## Parameters

- `applications`: An optional list of applications to include in the event. A small subset of popular App Store   apps have known associated web domains that get included implicitly. For example, an event that includes   an app implicitly includes usage of the app’s web domain.
- `categories`: An optional list of categories to include in the event.
- `webDomains`: An optional list of web domains to include in the event. Some web domains have associated apps included implicitly.
- `threshold`: The amount of time that results in a callback to a  .

## See Also

- [DeviceActivityEvent.Name](deviceactivityevent/name.md)
  The unique name of an event.
- [var includesAllActivity: Bool](deviceactivityevent/includesallactivity.md)
  A Boolean value that indicates whether the event includes all applications, categories, and web domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/init(applications:categories:webdomains:threshold:))*