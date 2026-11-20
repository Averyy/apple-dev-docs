# RefundItem

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

Information about the item to refund, such as its SKU, the type of refund, and whether to revoke entitlement.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object RefundItem
```

## Discussion

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

For a subscription that a customer buys as a multiseat purchase, you can’t combine a `refundType` of `CUSTOM` with a `revoke` value of `true`; the request fails with [`CustomRefundWithRevokeNotAllowedForMultiSeatSubscriptionError`](./customrefundwithrevokenotallowedformultiseatsubscriptionerror.md). Use a `refundType` of `FULL` or `PRORATED` to revoke a multiseat subscription. To revoke only some of its unclaimed seats, call the [`Revoke Subscription`](./revoke-subscription.md) endpoint with a [`revokeSeatQuantity`](./revokeseatquantity.md) instead.

## Properties

- `SKU` (SKU) *(required)*: **Maximum Length**: `128`
- `refundAmount` (refundAmount)
- `refundReason` (refundReason) *(required)*
- `refundType` (string) *(required)*: **Allowed Values**: `FULL`, `PRORATED`, `CUSTOM`
- `revoke` (boolean) *(required)*

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
- [object RequestRefundRequestV1](./requestrefundrequestv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/refunditem)*