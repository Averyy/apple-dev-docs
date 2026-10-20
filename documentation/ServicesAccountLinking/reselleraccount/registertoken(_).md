# registerToken(_:)

**Framework**: ServicesAccountLinking  
**Kind**: method  
**Role**: Type Method

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

> **Throws**: [`notEligible`](../registrationerror/noteligible.md) if app is not a registered partner, or [`failed`](../registrationerror/failed.md) for other failures

## Parameters

- `token`: The signed token representing user entitlement

## See Also

### Registration methods
- [static func registerIdentifier(String) async throws](./registeridentifier%28_%29.md)
  Registers an account identifier with the user’s Media & Purchases account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount/registertoken(_:))*