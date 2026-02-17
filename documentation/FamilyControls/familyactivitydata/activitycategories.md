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

The categories will have both the `localizedDisplayName` and `token` populated.

> ❗ **Important**: Your app must be authorized via [`AuthorizationCenter`](authorizationcenter.md) and data access must be available before attempting to access this variable or it will always throw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata/activitycategories)*