# eventType

**Framework**: External Purchase Server API  
**Kind**: typealias

The type of transaction the line item reports, whether it’s a buy or refund.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
string eventType
```

## Mentions

- [Reporting tokens with transactions](reportwithtransactions.md)

#### Discussion

Allowed values: `BUY`, `REFUND`

The `eventType` field describes the type of transaction of the line item. Specify an `eventType` in the line item objects [`OneTimeBuyLineItem`](onetimebuylineitem.md), [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md), and [`RefundLineItem`](refundlineitem.md).

Use the `eventType` values as follows:

- `BUY`: The line item describes a product purchase, such as a one-time buy, or a subscription event, including when there’s no charge, such as with a free trial. Use this value in the [`OneTimeBuyLineItem`](onetimebuylineitem.md) and [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md) objects.
- `REFUND`: The line item describes a refund or chargeback, up to the full amount of the `BUY` transaction in the [`referenceLineItemId`](referencelineitemid.md). Use this value in a [`RefundLineItem`](refundlineitem.md) object.

## See Also

- [type creationDate](creationdate.md)
  The UNIX date, in milliseconds, that the customer authorized the transaction.
- [type referenceLineItemId](referencelineitemid.md)
  The line item identifier of another transaction, that the report  references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/eventtype)*