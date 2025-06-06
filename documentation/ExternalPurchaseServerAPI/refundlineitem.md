# RefundLineItem

**Framework**: External Purchase Server API  
**Kind**: dictionary

The line item that indicates a refund transaction.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
object RefundLineItem
```

## Mentions

- [Reporting tokens with transactions](reportwithtransactions.md)
- [Reporting corrections](reportcorrections.md)

#### Discussion

Use a `RefundLineItem` to report either:

- A refund for a purchase transaction you previously submitted, or
- A correction to a refund you previously submitted

For more information about sending a report that includes refund line items, see [`Reporting tokens with transactions`](reportwithtransactions.md).

Report chargebacks as a refund.

## See Also

- [Reporting tokens with transactions](reportwithtransactions.md)
  Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.
- [Reporting corrections](reportcorrections.md)
  Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.
- [object OneTimeBuyLineItem](onetimebuylineitem.md)
  The line item that indicates a one-time charge transaction.
- [object SubscriptionBuyLineItem](subscriptionbuylineitem.md)
  The line item that indicates a subscription-related event or transaction.
- [Line item fields](lineitems.md)
  Properties that describe a single transaction or correction in an external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/refundlineitem)*