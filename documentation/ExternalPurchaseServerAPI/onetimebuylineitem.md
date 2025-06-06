# OneTimeBuyLineItem

**Framework**: External Purchase Server API  
**Kind**: dictionary

The line item that indicates a one-time charge transaction.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
object OneTimeBuyLineItem
```

## Mentions

- [Reporting tokens with transactions](reportwithtransactions.md)
- [Reporting corrections](reportcorrections.md)

#### Discussion

Use a `OneTimeBuyLineItem` to report a one-time charge transaction, or a correction to a one-time charge transaction that you previously submitted.

Each line-item object represents one transaction. Other types of line-item objects include:

- [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md), for reporting subscription-related transactions
- [`RefundLineItem`](refundlineitem.md), for reporting refunds

Include the line-item objects in the `lineItems` array of an [`ExternalPurchaseReport`](externalpurchasereport.md) object. To send the report, include the [`ExternalPurchaseReport`](externalpurchasereport.md) object in a request to the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint.

For more information, see [`Reporting tokens with transactions`](reportwithtransactions.md) and [`Reporting corrections`](reportcorrections.md).

## See Also

- [Reporting tokens with transactions](reportwithtransactions.md)
  Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.
- [Reporting corrections](reportcorrections.md)
  Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.
- [object RefundLineItem](refundlineitem.md)
  The line item that indicates a refund transaction.
- [object SubscriptionBuyLineItem](subscriptionbuylineitem.md)
  The line item that indicates a subscription-related event or transaction.
- [Line item fields](lineitems.md)
  Properties that describe a single transaction or correction in an external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/onetimebuylineitem)*