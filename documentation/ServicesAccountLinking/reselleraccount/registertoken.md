# registerToken(_:)

**Framework**: ServicesAccountLinking  
**Kind**: method

Registers a signed token with the user’s Media & Purchases account.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
@backDeployed(before: iOS 26.2)
static func registerToken(_ token: String) async throws
```

#### Discussion

> **Note**: [`notEligible`](registrationerror/noteligible.md) if app is not a registered partner, or [`failed`](registrationerror/failed.md) for other failures

## Parameters

- `token`: The signed token representing user entitlement

## See Also

- [static func registerIdentifier(String) async throws](reselleraccount/registeridentifier(_:).md)
  Registers an account identifier with the user’s Media & Purchases account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount/registertoken(_:))*