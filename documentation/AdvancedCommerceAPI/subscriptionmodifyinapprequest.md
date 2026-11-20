# SubscriptionModifyInAppRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request data your app provides to make changes to an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionModifyInAppRequest
```

## Mentions

- [Creating multiseat purchases](./creating-multiseat-purchases.md)
- [Advanced Commerce API changelog](./changelog.md)

## Discussion

You use the `SubscriptionModifyInAppRequest` in your app when the customer makes one or more changes to a subscription, such as upgrading, downgrading, adding or removing items, or adding seats.

### Example: upgrade a subscription

In the following request:

- The customer upgrades the subscription from a monthly to an annual subscription, effective immediately.
- The billing cycle resets.

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "2", 
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "e2a88501-25ba-403a-9c46-d7b8eecc56ba"
    },
    "currency": "USD", 
    "storefront": "USA",
    "effective": "IMMEDIATELY",
    "changeItems": [
        {
            "currentSKU": "ANNES_GOLD_TIER_1M",
            "SKU": "ANNES_PLATINUM_TIER_1Y",  
            "displayName": "Platinum Tier",
            "description": "Access to Anne's Game Stream & chat",
            "period": "P1Y",
            "price": 99990,
            "transactionId": "12345",
            "taxCode": "C003-00-1"
        }
    ]
}
```

### Example: downgrade a subscription at the next renewal

In the following request:

- The customer downgrades the subscription, effective at the next renewal.
- The billing cycle remains the same.

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "2", 
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "e2a88501-25ba-403a-9c46-d7b8eecc56ba"
    },
    "currency": "USD", 
    "storefront": "USA",
    "effective": "NEXT_BILL_CYCLE",
    "changeItems": [
        {
            "currentSKU": "ANNES_PLATINUM_TIER_1M",
            "SKU": "ANNES_GOLD_TIER_1M",  
            "displayName": "Gold Tier",
            "description": "Access to Anne's Game Stream",
            "period": "P1M",
            "price": 7990,
            "transactionId": "12345",
            "taxCode": "C003-00-1"
        }
    ]
}
```

### Example: Add seats to a group subscription

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

In the following request:

- The group purchaser adds 4 seats to a group subscription that has 8 seats, effective immediately.
- The change item identifies the item by its `currentSKU`, omits `SKU`, and re-declares the item’s current `seatPriceTiers` and `period`. Adding seats is the only change in the request.
- The `finalQuantity` is `12`, the total number of seats after the addition.
- The billing cycle remains the same. Apple calculates the prorated price for the added seats and presents a payment sheet to the group purchaser.
- The decoded signed transaction is the additional transaction for the 4 added seats. Its `quantity` is `4`, and its `additionalTransactionReason` is `SEAT_ADDITION`. Its `multiSeatInfo.priceTiers` lists the full per-seat prices of the tiers the added seats fall in, and the App Store prorates its `price` for the rest of the period.
- The original transaction for the first 8 seats stays valid and also reports an `additionalTransactionReason` of `SEAT_ADDITION`. The example doesn’t show it.
- The decoded signed renewal information shows the 12 seats that renew at the next renewal date, and the tiers that apply to them.
- The example doesn’t include optional fields in `requestInfo`.

**Request**:

```json
{
    "operation": "MODIFY_SUBSCRIPTION",
    "version": "2",
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36"
    },
    "currency": "USD",
    "storefront": "USA",
    "effective": "IMMEDIATELY",
    "changeItems": [
        {
            "currentSKU": "GROUP_PRO_1M",
            "displayName": "Group Pro",
            "description": "Shared access for your group",
            "period": "P1M",
            "seatPriceTiers": [
                { "maximumSeatQuantity": 5, "price": 9990 },
                { "maximumSeatQuantity": 5, "price": 7990 },
                { "price": 5990 }
            ],
            "finalQuantity": 12,
            "transactionId": "12345",
            "taxCode": "C003-00-1"
        }
    ]
}
```

**Decoded signed transaction**:

```json
{
    "transactionId": "12346",
    "originalTransactionId": "12345",
    "bundleId": "com.example",
    "productId": "com.example.base",
    "subscriptionGroupIdentifier": "34567",
    "purchaseDate": 1737014400000,
    "originalPurchaseDate": 1735718400000,
    "expiresDate": 1738396800000,
    "quantity": 4,
    "type": "Auto-Renewable Subscription",
    "inAppOwnershipType": "PURCHASED",
    "signedDate": 1737014400000,
    "environment": "Production",
    "transactionReason": "PURCHASE",
    "additionalTransactionReason": "SEAT_ADDITION",
    "storefront": "USA",
    "storefrontId": "143441",
    "price": 3610,
    "currency": "USD",
    "appTransactionId": "45678",
    "multiSeatInfo": {
        "invitationManagement": "APPLE",
        "priceTiers": [
            { "price": 7990, "quantity": 2 },
            { "price": 5990, "quantity": 2 }
        ]
    },
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "items": [
            {
                "SKU": "GROUP_PRO_1M",
                "displayName": "Group Pro",
                "description": "Shared access for your group",
                "price": 3610,
                "seatPriceTiers": [
                    { "maximumSeatQuantity": 5, "price": 9990 },
                    { "maximumSeatQuantity": 5, "price": 7990 },
                    { "price": 5990 }
                ]
            }
        ],
        "requestReferenceId": "c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36",
        "period": "P1M"
    }
}
```

**Decoded signed renewal information**:

```json
{
    "originalTransactionId": "12345",
    "autoRenewProductId": "com.example.base",
    "productId": "com.example.base",
    "autoRenewStatus": 1,
    "signedDate": 1737014400000,
    "environment": "Production",
    "recentSubscriptionStartDate": 1735718400000,
    "renewalDate": 1738396800000,
    "currency": "USD",
    "renewalPrice": 8490,
    "renewalQuantity": 12,
    "multiSeatInfo": {
        "renewalPriceTiers": [
            { "price": 9990, "quantity": 5 },
            { "price": 7990, "quantity": 5 },
            { "price": 5990, "quantity": 2 }
        ]
    },
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "items": [
            {
                "SKU": "GROUP_PRO_1M",
                "displayName": "Group Pro",
                "description": "Shared access for your group",
                "seatRenewalPriceTiers": [
                    { "maximumSeatQuantity": 5, "price": 9990 },
                    { "maximumSeatQuantity": 5, "price": 7990 },
                    { "price": 5990 }
                ]
            }
        ],
        "requestReferenceId": "c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36",
        "consistencyToken": "1.12345.c7e1f4a2-8b3d-4f6e-a9c1-5d2b8e0f7a36",
        "period": "P1M"
    },
    "appTransactionId": "45678"
}
```

## Properties

- `changeItems` ([SubscriptionModifyChangeItem]) *(required)*
- `currency` (currency) *(required)*
- `displayName` (displayName): **Maximum Length**: `30`
- `effective` (effective) *(required)*
- `operation` (string) *(required)*: **Allowed Values**: `MODIFY_SUBSCRIPTION`
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `transactionId` (transactionId) *(required)*
- `version` (version) *(required)*

## See Also

### Subscription modification in the app
- [object SubscriptionModifyAddItem](./subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyChangeItem](./subscriptionmodifychangeitem.md)
  The data your app provides to change an item of an auto-renewable subscription.
- [object ModifyBundleItem](./modifybundleitem.md)
- [object SubscriptionModifyRemoveItem](./subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](./subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.
- [object SubscriptionModifyInAppRequestV1](./subscriptionmodifyinapprequestv1.md)
- [object SubscriptionModifyChangeItemV1](./subscriptionmodifychangeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionmodifyinapprequest)*