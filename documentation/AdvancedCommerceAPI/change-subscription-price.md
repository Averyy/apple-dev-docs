# Change Subscription Price

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Increase or decrease the price of an auto-renewable subscription at the next renewal.

**Availability**:
- Advanced Commerce API 1.3+

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Handling subscription price changes](./handling-subscription-price-changes.md)
- [Authorizing API requests from your server](./authorizing-server-calls.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)
- [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md)

## Discussion

Call this endpoint when you change the price of a subscription or any bundle or item within it. For information about the customer communication, see [Handling subscription price changes](./handling-subscription-price-changes.md).

Only active subscriptions that aren’t in a billing retry state are eligible for price changes. When you call this endpoint, the price change takes effect at the next subscription renewal. Call the endpoint no later than 24 hours before the renewal date to have it take effect at the renewal.

For information about providing prices, see [Specifying prices for Advanced Commerce SKUs](./prices.md).

### Example request and response

In the following request:

- The subscription includes one item that has a price increase to USD 12.99.
- The price increase takes effect at the next subscription renewal.
- The decoded signed transaction shows price in the current period, before the increase.
- The decoded signed renewal information shows the increased price, which takes effect at the next renewal period if consented to.
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
            "SKU": "ANNES_GOLD_TIER_1M",
            "price": 12990
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
        "items": [
            {
                "SKU": "ANNES_GOLD_TIER_1M",
                "displayName": "Gold Tier",                        
                "description": "Access to Anne's Game Stream",
                "price": 9990
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
        "items": [
            {
                "SKU": "ANNES_GOLD_TIER_1M",
                "displayName": "Gold Tier",                        
                "description": "Access to Anne's Game Stream",
                "price": 12990,
                "priceIncreaseInfo": {
                    "status": "PENDING",
                    "price": 12990
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

### Example: Change the price tiers of a group subscription

> ❗ **Important**: Multiseat purchases are only available in the sandbox environment.

In the following request:

- The group subscription has 8 seats and uses volume discount pricing.
- The request lowers the price per seat of the second and last tiers. The price of the first tier doesn’t change.
- The item includes the complete `seatPriceTiers` array and no `price`. A price change doesn’t change the number of seats.
- The price change takes effect at the next subscription renewal.
- The decoded signed transaction shows the tiers that apply in the current period, before the change.
- The decoded signed renewal information shows the tiers that apply at the next renewal. The total price for the group purchaser’s seats is lower, so the change isn’t a price increase.
- The example doesn’t include the tax fields in `advancedCommerceInfo`.

**Request**:

```json
{
    "requestInfo": {
        "requestReferenceId": "4b6e9d1f-2a7c-4e3b-8f5a-6c1d0e9b2a47"
    },
    "currency": "USD",
    "storefront": "USA",
    "items": [
        {
            "SKU": "GROUP_PRO_1M",
            "seatPriceTiers": [
                { "maximumSeatQuantity": 5, "price": 9990 },
                { "maximumSeatQuantity": 5, "price": 6990 },
                { "price": 4990 }
            ]
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

**Response (decoded signed renewal information)**:

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
    "renewalPrice": 8865,
    "renewalQuantity": 8,
    "multiSeatInfo": {
        "renewalPriceTiers": [
            { "price": 9990, "quantity": 5 },
            { "price": 6990, "quantity": 3 }
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
                    { "maximumSeatQuantity": 5, "price": 6990 },
                    { "price": 4990 }
                ]
            }
        ],
        "requestReferenceId": "4b6e9d1f-2a7c-4e3b-8f5a-6c1d0e9b2a47",
        "consistencyToken": "1.12345.4b6e9d1f-2a7c-4e3b-8f5a-6c1d0e9b2a47",
        "period": "P1M"
    },
    "appTransactionId": "45678"
}
```

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v2/subscription/changePrice/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*: A transaction identifier of the auto-renewable subscription that is subject to the price change. Use the subscription’s original transaction ID or any subsequent transaction ID of a transaction related to the subscription.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionPriceChangeRequest`

The request body that contains the details of the price change.

## Responses

- `200` OK (`TransactionsResponse`, `application/json`): Success
- `400` Bad Request (`(FamilyTransactionNotSupportedError | InvalidTransactionIdError | NullRequestInfoError | NullItemsError | NullSKUError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | InvalidCurrencyError | NegativePriceError | SKULengthExceededError | InvalidProductError | InvalidSKUError | MismatchedStorefrontError | MissingPricingConfigForStorefrontError | OperationNotAllowedError | ItemCannotBeSpecifiedMultipleTimesError | PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError | InvalidSKUProvidedMustBeCurrentSKUSetToRenewError | ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError | NullPriceError | InvalidOperationError | TooManySeatPriceTiersError | InvalidMaximumSeatQuantityError | SeatPriceTiersNotDecreasingError | SeatPriceTiersNotAllowedForBundleError | PriceNotAllowedWithSeatPriceTiersError | SeatPriceTiersRequiredError | RepeatedRequestReferenceIdError | NullItemError | ProductAlreadyExistsError | InvalidAmountError | ChangeItemNotFoundError | NullAdvancedCommerceDataError | OfferPreventsItemMidCycleChangeError | ItemLimitExceededError)`, `application/json`)
- `401` Unauthorized (`UnauthorizedError`, `application/json`)
- `403` Forbidden (`(ForbiddenError | SubscriptionDoesNotExistError | SubscriptionNotEligibleError | ChangePriceOfBundleItemNotAllowedError)`, `application/json`)
- `404` Not Found (`(NotFoundError | TransactionIdNotFoundError)`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`)
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`)

## See Also

### Subscription price change from the server
- [object SubscriptionPriceChangeRequest](./subscriptionpricechangerequest.md)
  The request body you use to change the price of an auto-renewable subscription.
- [object SubscriptionPriceChangeResponse](./subscriptionpricechangeresponse.md)
  A response that contains signed JWS renewal and JWS transaction information after a subscription price change request.
- [object SubscriptionPriceChangeRequestV1](./subscriptionpricechangerequestv1.md)
- [object SubscriptionPriceChangeItemV1](./subscriptionpricechangeitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-price)*