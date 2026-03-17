# activityCategories

**Framework**: Family Controls  
**Kind**: property

The set of all possible activity categories.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
var activityCategories: Set<ActivityCategory> { get async throws }
```

#### Discussion

Each category contains both a `localizedDisplayName` and a `token`.

> ❗ **Important**:  Authorize your app with [`AuthorizationCenter`](AuthorizationCenter.md) and ensure data access is available before accessing this variable. Otherwise, it always throws an error.

## See Also

- [static let shared: FamilyActivityData](familyactivitydata/shared.md)
  A shared instance for accessing a person’s family activity data.
- [var installedApplications: [Application]](familyactivitydata/installedapplications.md)
  Applications someone installs on a device.
- [var visitedWebDomains: [WebDomain]](familyactivitydata/visitedwebdomains.md)
  Web domains someone visits on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata/activitycategories)*