# registerIdentifier(_:)

**Framework**: ServicesAccountLinking  
**Kind**: method

Registers an account identifier with the user’s Media & Purchases account.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+

## Declaration

```swift
@backDeployed(before: iOS 26.2)
static func registerIdentifier(_ identifier: String) async throws
```

#### Discussion

> **Note**: [`notEligible`](registrationerror/noteligible.md) if app is not a registered partner, or [`failed`](registrationerror/failed.md) for other failures.

## Parameters

- `identifier`: The UUID string representing user entitlement.

## See Also

- [static func registerToken(String) async throws](reselleraccount/registertoken(_:).md)
  Registers a signed token with the user’s Media & Purchases account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount/registeridentifier(_:))*