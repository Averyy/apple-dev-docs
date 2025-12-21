# revocationPercentage

**Framework**: App Store Server API  
**Kind**: typealias

The percentage, in milliunits, of the transaction that the App Store has refunded or revoked.

**Availability**:
- App Store Server API 1.19+

## Declaration

```swift
int32 revocationPercentage
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

The revocation percentage value is rounded to three decimal places of precision, and is expressed as an integer, in milliunits. This field is present in the [`JWSTransactionDecodedPayload`](jwstransactiondecodedpayload.md) for refunded transactions. This field doesn’t appear if the refund is reversed.

The following table shows several examples of revocation percentages, and their milliunit equivalents:

| Percentage | Integer equivalent, in milliunits |
| --- | --- |
| 67.932% | 67932 |
| 0.015% | 15 |
| 40% | 40000 |
| 100% | 100000 |

## See Also

- [type revocationDate](revocationdate.md)
  The UNIX time, in milliseconds, that the App Store refunded the transaction or revoked it from Family Sharing.
- [type revocationReason](revocationreason.md)
  The reason for a refunded transaction.
- [type revocationType](revocationtype.md)
  The type of the refund or revocation that applies to the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/revocationpercentage)*