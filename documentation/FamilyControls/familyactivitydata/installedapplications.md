# installedApplications

**Framework**: Family Controls  
**Kind**: property  
**Role**: Instance Property

Applications someone installs on a device.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var installedApplications: [Application] { get async throws }
```

## Discussion

Each application contains both a `bundleIdentifier` and a `token`.

> ❗ **Important**:  Authorize your app with [`AuthorizationCenter`](../authorizationcenter.md) and ensure data access is available before accessing this variable. Otherwise, it always throws an error.

## See Also

### Accessing activity data
- [static let shared: FamilyActivityData](./shared.md)
  A shared instance for accessing a person’s family activity data.
- [var activityCategories: Set<ActivityCategory>](./activitycategories.md)
  The set of all possible activity categories.
- [var visitedWebDomains: [WebDomain]](./visitedwebdomains.md)
  Web domains someone visits on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata/installedapplications)*