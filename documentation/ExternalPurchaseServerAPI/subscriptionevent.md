# subscriptionEvent

**Framework**: External Purchase Server API  
**Kind**: typealias

The event in the subscription’s life cycle that the transaction represents.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
string subscriptionEvent
```

## Mentions

- [Reporting tokens with transactions](reportwithtransactions.md)

#### Discussion

Allowed values: `SUBSCRIPTION_START`, `RENEWAL`, `SUBSCRIPTION_CHANGE`, `SUBSCRIPTION_PAYMENT`

Use the allowed values to indicate the subscription event in a [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md), as follows:

## See Also

- [type subscriptionDaysOfPaidService](subscriptiondaysofpaidservice.md)
  The total number of days of paid service for the subscription.
- [type subscriptionEndDate](subscriptionenddate.md)
  The UNIX date, in milli-seconds, the subscription renewal cycle ends.
- [type subscriptionStartDate](subscriptionstartdate.md)
  The UNIX date, in milli-seconds, of the start of the subscription renewal period.
- [type referenceLineItemId](referencelineitemid.md)
  The line item identifier of another transaction, that the report  references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/subscriptionevent)*