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

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "1", 
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "e2a88501-25ba-403a-9c46-d7b8eecc56ba"
    },
    "currency": "USD", 
    "storefront": "USA",
    "descriptors": {
        "effective": "IMMEDIATELY",
        "displayName": "Anne's Game Stream",
        "description": "Streaming Service for Anne's Game"
    },
    "periodChange": {
        "effective": "IMMEDIATELY",
        "period": "P1Y"
    },
    "retainBillingCycle": false,
    "changeItems": [
        {
            "effective": "IMMEDIATELY",
            "currentSKU": "ANNES_GOLD_TIER_1M",
            "SKU": "ANNES_PLATINUM_TIER_1Y",  
            "price": 99990,
            "displayName": "Platinum Tier",
            "description": "Access to Anne's Game Stream & chat",
            "reason": "UPGRADE"
        }
    ]
}
```

##### Example Add an Item and Retain the Billing Cycle

In the following request:

- The customer adds an item to the subscription, effective immediately.
- The billing cycle remains the same. The customer needs to pay the prorated price of the new item. Apple calculates the prorated price and presents a payment sheet to the customer.
- The customer is charged USD 4.99, as indicated by the `price` and `currency` fields in the request, at the next regular billing period.
- The example doesn’t include optional fields in `requestInfo`.

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "1", 
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "e2a88501-25ba-403a-9c46-d7b8eecc56ba"
    },
    "currency": "USD", 
    "storefront": "USA",
    "descriptors": {
        "effective": "IMMEDIATELY",
        "displayName": "Streaming Pass",
        "description": "Streaming pass with multiple items"
    },
    "retainBillingCycle": true,
    "addItems": [
        {
            "SKU": "NEWS_CHANNELS",    
            "displayName": "News Channel",                            
            "description": "Access to news channels",
            "price": 4990
        }
    ]
}
```

##### Example Remove an Item at the Next Renewal

In the following request:

- The customer removes an item from the subscription, effective at the next renewal.
- The billing cycle remains the same.
- The remaining items renew at the next billing period.
- The example doesn’t include optional fields in `requestInfo`.

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "1", 
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "e2a88501-25ba-403a-9c46-d7b8eecc56ba"
    },
    "currency": "USD", 
    "storefront": "USA",
    "retainBillingCycle": true,
    "removeItems": [
        {
            "SKU": "LIVE_SPORTS"
        }
    ]
}
```

##### Example Downgrade a Subscription at the Next Renewal

In the following request:

- The customer downgrades the subscription, effective at the next renewal.
- The billing cycle remains the same.
- The example doesn’t include optional fields in `requestInfo`.

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "1", 
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "e2a88501-25ba-403a-9c46-d7b8eecc56ba"
    },
    "currency": "USD", 
    "storefront": "USA",
    "descriptors": {
        "effective": "NEXT_BILL_CYCLE",
        "displayName": "Anne's Game Stream",
        "description": "Streaming Service for Anne’s Game"
    },
    "retainBillingCycle": true,
    "changeItems": [
        {
            "effective": "NEXT_BILL_CYCLE",
            "currentSKU": "ANNES_PLATINUM_TIER_1M",
            "SKU": "ANNES_GOLD_TIER_1M",  
            "price": 7990,
            "displayName": "Gold Tier",
            "description": "Access to Anne's Game Stream",
            "reason": "DOWNGRADE"
        }
    ]
}
```

## Properties

- `addItems` ([SubscriptionModifyAddItem])
- `changeItems` ([SubscriptionModifyChangeItem])
- `currency` (currency)
- `descriptors` (SubscriptionModifyDescriptors)
- `operation` (string) *(required)*
- `periodChange` (SubscriptionModifyPeriodChange)
- `removeItems` ([SubscriptionModifyRemoveItem])
- `requestInfo` (RequestInfo) *(required)*
- `retainBillingCycle` (retainBillingCycle) *(required)*
- `storefront` (storefront)
- `taxCode` (taxCode)
- `transactionId` (transactionId) *(required)*
- `version` (version) *(required)*

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