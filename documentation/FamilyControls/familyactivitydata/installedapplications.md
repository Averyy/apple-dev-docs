# installedApplications

**Framework**: Family Controls  
**Kind**: property

Applications someone installs on a device.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
var installedApplications: [Application] { get async throws }
```

#### Discussion

Each application contains both a `bundleIdentifier` and a `token`.

> ❗ **Important**:  Authorize your app with [`AuthorizationCenter`](AuthorizationCenter.md) and ensure data access is available before accessing this variable. Otherwise, it always throws an error.

## See Also

- [static let shared: FamilyActivityData](familyactivitydata/shared.md)
  A shared instance for accessing a person’s family activity data.
- [var activityCategories: Set<ActivityCategory>](familyactivitydata/activitycategories.md)
  The set of all possible activity categories.
- [var visitedWebDomains: [WebDomain]](familyactivitydata/visitedwebdomains.md)
  Web domains someone visits on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata/installedapplications)*