# revocationType

**Framework**: App Store Server API  
**Kind**: typealias

The type of the refund or revocation that applies to the transaction.

**Availability**:
- App Store Server API 1.19+

## Declaration

```swift
string revocationType
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

If the `revocationType` is `REFUND_PRORATED`, see the [`revocationPercentage`](revocationpercentage.md) for the prorated percentage.

## See Also

- [type revocationDate](revocationdate.md)
  The UNIX time, in milliseconds, that the App Store refunded the transaction or revoked it from Family Sharing.
- [type revocationReason](revocationreason.md)
  The reason for a refunded transaction.
- [type revocationPercentage](revocationpercentage.md)
  The percentage, in milliunits, of the transaction that the App Store has refunded or revoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/revocationtype)*