# init(applications:categories:webDomains:threshold:includesPastActivity:)

**Framework**: DeviceActivity  
**Kind**: init

Creates a new event.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
init(applications: Set<ApplicationToken> = [], categories: Set<ActivityCategoryToken> = [], webDomains: Set<WebDomainToken> = [], threshold: DateComponents, includesPastActivity: Bool)
```

#### Discussion

An application’s extension receives a callback once the combination of specified [`applications`](deviceactivityevent/applications.md), [`categories`](deviceactivityevent/categories.md), and [`webDomains`](deviceactivityevent/webdomains.md) have been in use longer than the event’s threshold within the activity’s scheduled interval. If your app didn’t specify any `applications`, `categories`, or `webDomains`, the event includes all `applications`, `categories`, and `web domains`.

## Parameters

- `applications`: An optional list of applications to include in the event. A small subset of popular App Store   apps have known associated web domains that get included implicitly. For example, an event that includes   an app implicitly includes usage of the app’s web domain.
- `categories`: An optional list of categories to include in the event.
- `webDomains`: An optional list of web domains to include in the event. Some web domains have associated apps included implicitly.
- `threshold`: The amount of time that results in a callback to a  .
- `includesPastActivity`: Whether the system takes into account the person’s device activity before your app starts monitoring the event.   For example, if your app calls   at 1:30pm with a schedule   of 1:00pm to 2:00pm, then this boolean determines whether any activity between 1:00 PM and 1:30 PM will contribute to its threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/deviceactivity/deviceactivityevent/init(applications:categories:webdomains:threshold:includespastactivity:))*