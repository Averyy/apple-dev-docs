# Change Subscription Price

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Increase or decrease the price of an auto-renewable subscription, a bundle, or individual items within a subscription at the next renewal.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Handling subscription price changes](handling-subscription-price-changes.md)
- [Authorizing API requests from your server](authorizing-server-calls.md)
- [Advanced Commerce API changelog](changelog.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)

#### Discussion

Call this endpoint when you change the price of a subscription or any bundle or item within it. For information about the customer communication, see [`Handling subscription price changes`](handling-subscription-price-changes.md).

Only active subscriptions that aren’t in a billing retry state are eligible for price changes. When you call this endpoint, the price change takes effect at the next subscription renewal. Call the endpoint no later than 24 hours before the renewal date to have it take effect at the renewal.

For information about providing prices, see [`Specifying prices for Advanced Commerce SKUs`](prices.md).

##### Example Request and Response

In the following request:

- The subscription includes multiple items, and only one item has a price increase to USD 12.99.
- The price increase takes effect at the next subscription renewal.
- The decoded signed transaction shows price in the current period, before the increase.
- The decoded signed renewal information shows the increased price, which takes effect at the next renewal period if consented to.
- The item has a dependent SKU, which will be cancelled if the price increase is not agreed to.
- In this example, the price increase has been communicated, so the status is marked as pending.

**Request**:

```json
{
    "requestInfo": {
        "requestReferenceId": "7c80bb86-f892-4b21-a919-1357811d6c4f"
    },
    "currency": "USD",
    "storefront": "USA",
    "items": [
        { 
            "SKU": "AD_FREE_1M",
            "price": 12990,
            "dependentSKUs": ["ADVANCED_FEATURES_1M"]
        } 
    ]
}
```

**Response (decoded signed transaction)**:

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
    "quantity": 1,
    "type": "Auto-Renewable Subscription",
    "inAppOwnershipType": "PURCHASED",
    "signedDate": 1735718400000,
    "environment": "Production",
    "transactionReason": "PURCHASE",
    "storefront": "USA",
    "storefrontId": "143441",
    "price": 12980,
    "currency": "USD",
    "appTransactionId": "45678",
    "appAccountToken": "3152947d-8f63-41c2-9a91-e92e45f145e9",
    "advancedCommerceInfo": {
        "estimatedTax": 0,
        "taxRate": "0",
        "taxCode": "C003-00-1",
        "taxExclusivePrice": 12980,
        "descriptors": {
            "displayName": "Ad-free and advanced feature package",
            "description": "Remove ads and unlock advanced features."
        },
        "items": [
            {
                "SKU": "AD_FREE_1M",
                "displayName": "Ad-free monthly plan",                        
                "description": "Remove ads for the service.",
                "price": 9990
            },
            {
                "SKU": "ADVANCED_FEATURES_1M",
                "displayName": "Advanced feature monthly plan",
                "description": "Unlock advanced features for the month.",
                "price": 3990,
                "offer": {
                    "price": 2990, 
                    "period": "P1M",
                    "periodCount": 3,
                    "reason": "ACQUISITION"
                }
            }
        ],
        "requestReferenceId": "932c6903-0ab8-4469-9f21-015f6fab013c",
        "period": "P1M"
    }
}
```

**Response (decoded signed renewal information)**:

```json
{
    "originalTransactionId": "12345",
    "autoRenewProductId": "com.example.base",
    "productId": "com.example.base",
    "autoRenewStatus": 1,
    "signedDate": 1735718400000,
    "environment": "Production",
    "recentSubscriptionStartDate": 1735718400000,
    "renewalDate": 1738396800000,
    "advancedCommerceInfo": {
        "taxCode": "C003-00-1",
        "descriptors": {
            "displayName": "Ad-free and advanced feature package",
            "description": "Remove ads and unlock advanced features."
        },
        "items": [
            {
                "SKU": "AD_FREE_1M",
                "displayName": "Ad-free monthly plan",                        
                "description": "Remove ads for the service.",
                "price": 12990,
                "priceIncreaseInfo": {
                    "status": "PENDING",
                    "price": 12990,
                    "dependentSKUs": ["ADVANCED_FEATURES_1M"]
                }
            },
            {
                "SKU": "ADVANCED_FEATURES_1M",
                "displayName": "Advanced feature monthly plan",
                "description": "Unlock advanced features for the month.",
                "price": 3990,
                "offer": {
                    "price": 2990, 
                    "period": "P1M",
                    "periodCount": 2,
                    "reason": "ACQUISITION"
                }
            }
        ],
        "requestReferenceId": "932c6903-0ab8-4469-9f21-015f6fab013c",
        "consistencyToken": "1.12345.932c6903-0ab8-4469-9f21-015f6fab013c",
        "period": "P1M"
    },
    "appTransactionId": "45678",
    "appAccountToken": "3152947d-8f63-41c2-9a91-e92e45f145e9"
}
```

## Endpoint

`POST https://api.storekit-sandbox.itunes.apple.com/advancedCommerce/v1/subscription/changePrice/{transactionId}`

## Parameters

- `transactionId` (string) *(required)*: A transaction identifier of the auto-renewable subscription that is subject to the price change. Use the subscription’s original transaction ID or any subsequent transaction ID of a transaction related to the subscription.

## Request Body

The request body that contains the details of the price change.

## See Also

- [object SubscriptionPriceChangeRequest](subscriptionpricechangerequest.md)
  The request body you use to change the price of an auto-renewable subscription.
- [object SubscriptionPriceChangeResponse](subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-price)*