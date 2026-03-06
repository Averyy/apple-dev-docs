# RequestRefundResponse

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The response body for a transaction refund request.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
object RequestRefundResponse
```

#### Overview

##Discussion This is the response body for the [`Request Transaction Refund`](request-transaction-refund.md) endpoint.

## Properties

- `signedRenewalInfo` (JWSRenewalInfo): Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- `signedTransactionInfo` (JWSTransaction) *(required)*: Transaction information signed by the App Store, in JWS Compact Serialization format.

## See Also

- [Request Transaction Refund](request-transaction-refund.md)
  Request a refund for a one-time charge or subscription transaction.
- [object RequestRefundRequest](requestrefundrequest.md)
  The request body for requesting a refund for a transaction.
- [object RequestRefundItem](requestrefunditem.md)
  Information about the refund request for an item, such as its SKU, the refund amount, reason, and type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/requestrefundresponse)*