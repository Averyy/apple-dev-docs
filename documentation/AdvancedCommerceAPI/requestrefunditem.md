# RequestRefundItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary

Information about the refund request for an item, such as its SKU, the refund amount, reason, and type.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
object RequestRefundItem
```

## Properties

- `SKU` (SKU) *(required)*: The product identifier.
- `refundAmount` (refundAmount): The refund amount you’re requesting for the `SKU`, in milliunits of the currency.
- `refundReason` (refundReason) *(required)*: The reason for the refund request.
- `refundType` (string) *(required)*: The type of refund requested.
- `revoke` (boolean) *(required)*

## See Also

- [Request Transaction Refund](request-transaction-refund.md)
  Request a refund for a one-time charge or subscription transaction.
- [object RequestRefundRequest](requestrefundrequest.md)
  The request body for requesting a refund for a transaction.
- [object RequestRefundResponse](requestrefundresponse.md)
  The response body for a transaction refund request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/requestrefunditem)*