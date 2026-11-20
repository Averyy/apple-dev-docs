# SubscriptionCreateRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request data your app provides when a customer purchases an auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionCreateRequest
```

## Mentions

- [Creating SKUs for your Apple In-App Purchases](./creating-your-purchases.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)
- [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md)
- [Advanced Commerce API changelog](./changelog.md)

### Example: Create a subscription

```json
{
    "operation": "CREATE_SUBSCRIPTION",
    "version": "2", 
    "requestInfo": {
        "requestReferenceId": "74ad2401-488d-4e1a-9c9d-80cdf0efed67"
    },
    "currency": "USD", 
    "taxCode": "C003-00-1", 
    "storefront": "USA",
    "items": [ 
        {
            "SKU": "ANNES_GOLD_TIER_1M",
            "displayName": "Gold Tier",                        
            "description": "Access to Anne's Game Stream",
            "period": "P1M",
            "price": 7990
        }
    ]
}
```

### Example: Create a group subscription with per-seat pricing

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

In the following request:

- The group purchaser buys 3 seats of a group subscription with per-seat pricing, where every seat has the same price.
- The item’s `seatPriceTiers` array contains a single tier, which doesn’t include a `maximumSeatQuantity`. The item doesn’t include a `price`.
- The `finalQuantity` is `3`, the number of seats the group purchaser buys.
- The decoded signed transaction reports the number of seats in `quantity`, and `multiSeatInfo.priceTiers` reports the 3 seats at the tier’s price.
- The example doesn’t include optional fields in `requestInfo` or the tax fields in `advancedCommerceInfo`.

**Request**:

```json
{
    "operation": "CREATE_SUBSCRIPTION",
    "version": "2",
    "requestInfo": {
        "requestReferenceId": "3f8b2c1d-6e4a-4b7f-9d2e-1a5c8b0f4e62"
    },
    "currency": "USD",
    "taxCode": "C003-00-1",
    "storefront": "USA",
    "items": [
        {
            "SKU": "GROUP_PRO_1M",
            "displayName": "Group Pro",
            "description": "Shared access for your group",
            "period": "P1M",
            "seatPriceTiers": [
                { "price": 9990 }
            ],
            "finalQuantity": 3
        }
    ]
}
```

**Decoded signed transaction**:

```json
{
    "transactionId": "12345",
    "originalTransactionId": "12345",
    "webOrderLineItemId": "23456",
    "bundleId": "com.example",
    "productId": "com.example.base",
    "subscriptionGroupIdentifier": "34567",
    "purchaseDate": 1735718400000,
    "originalPurchaseDate": 1735718400000,
    "expiresDate": 1738396800000,
    "quantity": 3,
    "type": "Auto-Renewable Subscription",
    "inAppOwnershipType": "PURCHASED",
    "signedDate": 1735718400000,
    "environment": "Production",
    "transactionReason": "PURCHASE",
    "storefront": "USA",
    "storefrontId": "143441",
    "price": 9990,
    "currency": "USD",
    "appTransactionId": "45678",
    "multiSeatInfo": {
        "invitationManagement": "APPLE",
        "priceTiers": [
            { "price": 9990, "quantity": 3 }
        ]
    },
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "items": [
            {
                "SKU": "GROUP_PRO_1M",
                "displayName": "Group Pro",
                "description": "Shared access for your group",
                "price": 9990,
                "seatPriceTiers": [
                    { "price": 9990 }
                ]
            }
        ],
        "requestReferenceId": "3f8b2c1d-6e4a-4b7f-9d2e-1a5c8b0f4e62",
        "period": "P1M"
    }
}
```

### Example: Create a group subscription with volume discount pricing

In the following request:

- The group purchaser buys 8 seats of a group subscription with volume discount pricing, where the price per seat decreases as the number of seats increases.
- The item’s `seatPriceTiers` array contains three tiers, from the most expensive to the least expensive. The first two tiers each cover 5 seats, and the last tier covers every seat after the tenth.
- The purchase includes 5 seats at the first tier’s price and 3 seats at the second tier’s price. The request still includes the last tier.
- The item doesn’t include a `price`, and its `finalQuantity` is `8`.
- In the decoded signed transaction, `multiSeatInfo.priceTiers` lists the seats the purchase includes at each price, and `price` is the average price per seat.
- The example doesn’t include optional fields in `requestInfo` or the tax fields in `advancedCommerceInfo`.

**Request**:

```json
{
    "operation": "CREATE_SUBSCRIPTION",
    "version": "2",
    "requestInfo": {
        "requestReferenceId": "9a4d7e2b-1c3f-4e8a-b5d6-0f2e7c9a1b34"
    },
    "currency": "USD",
    "taxCode": "C003-00-1",
    "storefront": "USA",
    "items": [
        {
            "SKU": "GROUP_PRO_1M",
            "displayName": "Group Pro",
            "description": "Shared access for your group",
            "period": "P1M",
            "seatPriceTiers": [
                { "maximumSeatQuantity": 5, "price": 9990 },
                { "maximumSeatQuantity": 5, "price": 7990 },
                { "price": 5990 }
            ],
            "finalQuantity": 8
        }
    ]
}
```

**Decoded signed transaction**:

```json
{
    "transactionId": "12345",
    "originalTransactionId": "12345",
    "webOrderLineItemId": "23456",
    "bundleId": "com.example",
    "productId": "com.example.base",
    "subscriptionGroupIdentifier": "34567",
    "purchaseDate": 1735718400000,
    "originalPurchaseDate": 1735718400000,
    "expiresDate": 1738396800000,
    "quantity": 8,
    "type": "Auto-Renewable Subscription",
    "inAppOwnershipType": "PURCHASED",
    "signedDate": 1735718400000,
    "environment": "Production",
    "transactionReason": "PURCHASE",
    "storefront": "USA",
    "storefrontId": "143441",
    "price": 9240,
    "currency": "USD",
    "appTransactionId": "45678",
    "multiSeatInfo": {
        "invitationManagement": "APPLE",
        "priceTiers": [
            { "price": 9990, "quantity": 5 },
            { "price": 7990, "quantity": 3 }
        ]
    },
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "items": [
            {
                "SKU": "GROUP_PRO_1M",
                "displayName": "Group Pro",
                "description": "Shared access for your group",
                "price": 9240,
                "seatPriceTiers": [
                    { "maximumSeatQuantity": 5, "price": 9990 },
                    { "maximumSeatQuantity": 5, "price": 7990 },
                    { "price": 5990 }
                ]
            }
        ],
        "requestReferenceId": "9a4d7e2b-1c3f-4e8a-b5d6-0f2e7c9a1b34",
        "period": "P1M"
    }
}
```

## Properties

- `currency` (currency) *(required)*
- `displayName` (displayName): **Maximum Length**: `30`
- `items` ([SubscriptionCreateItem]) *(required)*
- `operation` (string) *(required)*: **Allowed Values**: `CREATE_SUBSCRIPTION`
- `period` (period)
- `principalAppAppleId` (int64)
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `taxCode` (taxCode)
- `version` (version) *(required)*

## See Also

### Subscription creation in the app
- [object SubscriptionCreateItem](./subscriptioncreateitem.md)
  The data that describes a subscription item.
- [object BundleItem](./bundleitem.md)
- [object SubscriptionCreateRequestV1](./subscriptioncreaterequestv1.md)
- [object SubscriptionCreateItemV1](./subscriptioncreateitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptioncreaterequest)*