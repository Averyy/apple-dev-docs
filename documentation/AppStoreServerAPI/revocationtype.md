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

A `revocationType` of `ASSIGNMENT_REVOKE` indicates that the organization or group purchaser removed the subscription from a customer. Revoke the customer’s access to the content the transaction provides. For more information about assignment, see [`Get Customer Groups`](get-customer-groups.md).

## See Also

- [type revocationDate](revocationdate.md)
  The UNIX time, in milliseconds, that the App Store refunded the transaction or revoked it from Family Sharing.
- [type revocationReason](revocationreason.md)
  The reason for a refunded transaction.
- [type revocationPercentage](revocationpercentage.md)
  The percentage, in milliunits, of the transaction that the App Store has refunded or revoked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/revocationtype)*