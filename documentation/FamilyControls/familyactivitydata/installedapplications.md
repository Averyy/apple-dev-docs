# installedApplications

**Framework**: Family Controls  
**Kind**: property

An array of applications installed by the current user.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
var installedApplications: [Application] { get async throws }
```

#### Discussion

The applications will have both the `bundleIdentifier` and `token` populated.

> ❗ **Important**: Your app must be authorized via [`AuthorizationCenter`](authorizationcenter.md) and data access must be available before attempting to access this variable or it will always throw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata/installedapplications)*