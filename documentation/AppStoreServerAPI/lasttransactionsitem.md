# lastTransactionsItem

**Framework**: App Store Server API  
**Kind**: dictionary

The most recent App Store-signed transaction information and App Store-signed renewal information for an auto-renewable subscription.

**Availability**:
- App Store Server API 1.0+

## Declaration

```swift
object lastTransactionsItem
```

## Topics

### Data Types
- [type originalTransactionId](originaltransactionid.md)
  The original transaction identifier of a purchase.
- [type status](status.md)
  The status of an auto-renewable subscription.
- [type JWSRenewalInfo](jwsrenewalinfo.md)
  Subscription renewal information, signed by the App Store, in JSON Web Signature (JWS) format.
- [type JWSTransaction](jwstransaction.md)
  Transaction information signed by the App Store, in JSON Web Signature (JWS) Compact Serialization format.

## See Also

- [subscriptionGroupIdentifier](subscriptiongroupidentifieritem/subscriptiongroupidentifier.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/lasttransactionsitem)*