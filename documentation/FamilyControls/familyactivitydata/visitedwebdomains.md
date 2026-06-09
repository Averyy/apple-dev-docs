# visitedWebDomains

**Framework**: Family Controls  
**Kind**: property

Web domains someone visits on their device.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
var visitedWebDomains: [WebDomain] { get async throws }
```

#### Discussion

Each web domain contains both a `domain` and a `token`.

> ❗ **Important**:  Authorize your app with [`AuthorizationCenter`](AuthorizationCenter.md) and ensure data access is available before accessing this variable. Otherwise, it will always throw an error.

## See Also

- [static let shared: FamilyActivityData](familyactivitydata/shared.md)
  A shared instance for accessing a person’s family activity data.
- [var activityCategories: Set<ActivityCategory>](familyactivitydata/activitycategories.md)
  The set of all possible activity categories.
- [var installedApplications: [Application]](familyactivitydata/installedapplications.md)
  Applications someone installs on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata/visitedwebdomains)*