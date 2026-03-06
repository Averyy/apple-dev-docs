# Cancel a Subscription

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Turn off automatic renewal to cancel a customer’s auto-renewable subscription.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Authorizing API requests from your server](authorizing-server-calls.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)

#### Discussion

When this endpoint succeeds, the system sets the subscription’s auto-renew status to `false` and the subscription doesn’t renew at the next renewal period. The customer continues to have access to the subscription until the end of the current period.

To immediately cancel a subscription instead, see [`Revoke Subscription`](revoke-subscription.md).

> **Note**: To use the `Cancel a Subscription` endpoint, your membership Account Holder must sign the Advanced Commerce API Addendum, and you must meet certain eligibility requirements. For more information, see [`Advanced Commerce API`](https://developer.apple.comhttps://developer.apple.com/in-app-purchase/advanced-commerce-api/). If the most recent version of this agreement isn’t yet accepted, you can’t call this endpoint, and it returns an error.

Refer to the Advanced Commerce API Addendum to learn the use cases for the `Cancel a Subscription`, [`Revoke Subscription`](revoke-subscription.md), and [`Request Transaction Refund`](request-transaction-refund.md) APIs.

##### Example Request and Response

**Request**:

```json
{
    "requestInfo": {
        "requestReferenceId": "932c6903-0ab8-4469-9f21-015f6fab013c"
    },
    "storefront": "USA"  
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
    "autoRenewStatus": 0,
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

`POST https://api.storekit-sandbox.itunes.apple.com/advancedCommerce/v1/subscription/cancel/{transactionId}`

## Parameters

- `transactionId` (string) *(required)*: The transaction identifier of the auto-renewable subscription to cancel.

## Request Body

The request body that includes information about the subscription to cancel.

## See Also

- [object SubscriptionCancelRequest](subscriptioncancelrequest.md)
  The request body for turning off automatic renewal of a subscription.
- [object SubscriptionCancelResponse](subscriptioncancelresponse.md)
  The response body for a successful subscription cancellation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/cancel-a-subscription)*