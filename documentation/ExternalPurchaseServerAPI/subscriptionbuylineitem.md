# SubscriptionBuyLineItem

**Framework**: External Purchase Server API  
**Kind**: dictionary

The line item that indicates a subscription-related event or transaction.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
object SubscriptionBuyLineItem
```

## Mentions

- [Reporting tokens with transactions](reportwithtransactions.md)
- [Reporting corrections](reportcorrections.md)

#### Discussion

Use a `SubscriptionBuyLineItem` to report a subscription-related transaction or event, or a correction to the same.

Each line-item object represents one transaction. Other types of line-item objects include:

- [`OneTimeBuyLineItem`](onetimebuylineitem.md), for reporting a one-time charge
- [`RefundLineItem`](refundlineitem.md), for reporting refunds

Include the line-item objects in the `lineItems` array of an [`ExternalPurchaseReport`](externalpurchasereport.md) object. To send the report, include the [`ExternalPurchaseReport`](externalpurchasereport.md) object in a request to the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint.

> **Note**: Identify a subscription using the [`lineItemId`](lineitemid.md) of the original subscription-start transaction. A line item for a subscription start has an [`eventType`](eventtype.md) of `BUY` and a [`subscriptionEvent`](subscriptionevent.md) of `SUBSCRIPTION_START`.

For example, to report a renewal for a subscription, set the renewal transaction’s [`referenceLineItemId`](referencelineitemid.md) to the `lineItemId` of the subscription-start line item, and set the  `subscriptionEvent` to `RENEWAL`.

For more information, see [`Reporting tokens with transactions`](reportwithtransactions.md) and [`Reporting corrections`](reportcorrections.md).

## See Also

- [Reporting tokens with transactions](reportwithtransactions.md)
  Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.
- [Reporting corrections](reportcorrections.md)
  Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.
- [object OneTimeBuyLineItem](onetimebuylineitem.md)
  The line item that indicates a one-time charge transaction.
- [object RefundLineItem](refundlineitem.md)
  The line item that indicates a refund transaction.
- [Line item fields](lineitems.md)
  Properties that describe a single transaction or correction in an external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/subscriptionbuylineitem)*