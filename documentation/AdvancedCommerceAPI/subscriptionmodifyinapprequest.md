# SubscriptionModifyInAppRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The request data your app provides to make changes to an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
object SubscriptionModifyInAppRequest
```

#### Discussion

You use the `SubscriptionModifyInAppRequest` in your app when the customer makes one or more changes to a subscription, such as upgrading, downgrading, or adding or removing items.

##### Example Upgrade a Subscription

In the following request:

- The customer upgrades the subscription from a monthly to an annual subscription, effective immediately.
- The billing cycle resets.
- The example doesn’t include optional fields in `requestInfo`.

##### Example Add an Item and Retain the Billing Cycle

In the following request:

- The customer adds an item to the subscription, effective immediately.
- The billing cycle remains the same. The customer needs to pay the prorated price of the new item. Apple calculates the prorated price and presents a payment sheet to the customer.
- The customer is charged USD 4.99, as indicated by the `price` and `currency` fields in the request, at the next regular billing period.
- The example doesn’t include optional fields in `requestInfo`.

##### Example Remove an Item at the Next Renewal

In the following request:

- The customer removes an item from the subscription, effective at the next renewal.
- The billing cycle remains the same.
- The remaining items renew at the next billing period.
- The example doesn’t include optional fields in `requestInfo`.

##### Example Downgrade a Subscription at the Next Renewal

In the following request:

- The customer downgrades the subscription, effective at the next renewal.
- The billing cycle remains the same.
- The example doesn’t include optional fields in `requestInfo`.

## See Also

- [object SubscriptionModifyAddItem](subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyChangeItem](subscriptionmodifychangeitem.md)
  The data your app provides to change an item of an auto-renewable subscription.
- [object SubscriptionModifyRemoveItem](subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyinapprequest)*