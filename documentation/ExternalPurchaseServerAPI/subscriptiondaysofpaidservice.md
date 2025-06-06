# subscriptionDaysOfPaidService

**Framework**: External Purchase Server API  
**Kind**: typealias

The total number of days of paid service for the subscription.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
int32 subscriptionDaysOfPaidService
```

#### Discussion

Provide the days of paid service for the subscription, calculating it as follows:

- For a new subscription, the days of paid service begins at `0` on the date a customer subscribes.
- When the subscription renews, add the number of paid days to the `subscriptionDaysOfPaidService` value.
- If you report a `SUBSCRIPTION_CHANGE` [`subscriptionEvent`](subscriptionevent.md), continue to accumulate the days of paid service.
- Don’t include days that the customer doesn’t pay for in the `subscriptionDaysOfPaidService` value. Unpaid days include free trials, or other offers or extensions of service that customers don’t pay for.

The days of paid service stop accumulating when:

- The customer cancels the subscription.
- You inactivate the subscription due to a payment issue.

## See Also

- [type subscriptionEndDate](subscriptionenddate.md)
  The UNIX date, in milli-seconds, the subscription renewal cycle ends.
- [type subscriptionEvent](subscriptionevent.md)
  The event in the subscription’s life cycle that the transaction represents.
- [type subscriptionStartDate](subscriptionstartdate.md)
  The UNIX date, in milli-seconds, of the start of the subscription renewal period.
- [type referenceLineItemId](referencelineitemid.md)
  The line item identifier of another transaction, that the report  references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/subscriptiondaysofpaidservice)*