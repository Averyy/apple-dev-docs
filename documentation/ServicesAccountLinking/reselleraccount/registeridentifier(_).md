# registerIdentifier(_:)

**Framework**: ServicesAccountLinking  
**Kind**: method  
**Role**: Type Method

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

## Discussion

> **Throws**: [`notEligible`](../registrationerror/noteligible.md) if app is not a registered partner, or [`failed`](../registrationerror/failed.md) for other failures.

## Parameters

- `identifier`: The UUID string representing user entitlement.

## See Also

### Registration methods
- [static func registerToken(String) async throws](./registertoken%28_%29.md)
  Registers a signed token with the user’s Media & Purchases account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicesaccountlinking/reselleraccount/registeridentifier(_:))*