# transactionReason

**Framework**: App Store Server API  
**Kind**: typealias

The cause of a purchase transaction, which indicates whether it’s a customer’s purchase or a renewal for an auto-renewable subscription that the system initiates.

**Availability**:
- App Store Server API 1.8+

## Declaration

```swift
string transactionReason
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

If a customer upgrades an auto-renewable subscription, the upgrade is effective immediately and the `transactionReason` is `PURCHASE`.

If a customer downgrades an auto-renewable subscription, the product change occurs on the subscription renewal date. The resulting `transactionReason` is `RENEWAL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/transactionreason)*