# revocationReason

**Framework**: App Store Server API  
**Kind**: typealias

The reason for a refunded transaction.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
int32 revocationReason
```

#### Discussion

For Family Sharing transactions, the revocation reason value is `0` if the customer leaves the family group or the owner stops sharing. If the purchaser of a Family Sharing transaction receives a refund, the revocation reason for Family Sharing transactions matches the value of the purchaser’s revocation reason.

## See Also

- [type revocationDate](revocationdate.md)
  The UNIX time, in milliseconds, that the App Store refunded the transaction or revoked it from Family Sharing.
- [type revocationPercentage](revocationpercentage.md)
  The percentage, in milliunits, of the transaction that the App Store has refunded or revoked.
- [type revocationType](revocationtype.md)
  The type of the refund or revocation that applies to the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/revocationreason)*