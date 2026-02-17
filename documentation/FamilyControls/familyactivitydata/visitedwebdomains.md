# visitedWebDomains

**Framework**: Family Controls  
**Kind**: property

An array of web domains visited by the current user.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
var visitedWebDomains: [WebDomain] { get async throws }
```

#### Discussion

The web domains will have both the `domain` and `token` populated.

> ❗ **Important**: Your app must be authorized via [`AuthorizationCenter`](authorizationcenter.md) and data access must be available before attempting to access this variable or it will always throw.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitydata/visitedwebdomains)*