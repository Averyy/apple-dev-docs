# revocationType

**Framework**: App Store Server Notifications  
**Kind**: typealias

The type of the refund or revocation that applies to the transaction.

**Availability**:
- App Store Server Notifications 2.20+

## Declaration

```swift
string revocationType
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

If the `revocationType` is `REFUND_PRORATED`, see the [`revocationPercentage`](revocationpercentage.md) for the prorated percentage.

## See Also

- [type revocationDate](revocationdate.md)
  The UNIX time, in milliseconds, that the App Store refunded the transaction or revoked it from Family Sharing.
- [type revocationPercentage](revocationpercentage.md)
  The percentage, in milliunits, of the transaction that the App Store has refunded or revoked.
- [type revocationReason](revocationreason.md)
  The reason for a revoked or refunded transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/revocationtype)*