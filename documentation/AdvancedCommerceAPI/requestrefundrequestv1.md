# RequestRefundRequestV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```
object RequestRefundRequestV1
```

## Properties

- `currency` (currency)
- `items` ([RequestRefundItem]) *(required)*
- `refundRiskingPreference` (refundRiskingPreference) *(required)*
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)

## See Also

### Refund request from the server
- [Request Transaction Refund](./request-transaction-refund.md)
  Request a refund for a one-time charge or subscription transaction.
- [object RequestRefundRequest](./requestrefundrequest.md)
  The request body for requesting a refund for a transaction.
- [object RequestRefundResponse](./requestrefundresponse.md)
  The response body for a transaction refund request.
- [object RequestRefundItem](./requestrefunditem.md)
  Information about the refund request for an item, such as its SKU, the refund amount, reason, and type.
- [object RefundItem](./refunditem.md)
  Information about the item to refund, such as its SKU, the type of refund, and whether to revoke entitlement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/requestrefundrequestv1)*