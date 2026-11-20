# Change Subscription Metadata

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the SKU, display name, and description associated with a subscription, without affecting the subscription’s billing or its service.

**Availability**:
- Advanced Commerce API 1.3+

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Authorizing API requests from your server](./authorizing-server-calls.md)
- [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md)

## Discussion

Use this endpoint to update the display name and description of an auto-renewable subscription. Calling this endpoint doesn’t change the price, billing details, or the service. For example, you can call `Change Subscription Metadata` if a subscription’s display name changes due to a change in its branding.

Don’t call this endpoint if a customer is changing subscriptions to receive a different service, such as upgrading, downgrading, or cross-grading. For such changes, use [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md).

### Example request and response

In the following request:

- The subscription item’s display name and SKU were previously “Basic Tier” and “BASIC_TIER_1M”.
- The change subscription metadata request updates the display name to “Basic Plan” and the SKU to “BASIC_PLAN_1M”.
- The decoded signed transaction shows previous display name “Basic Tier” that the customer purchased.
- The decoded signed renewal information shows the display name “Basic Plan” that the subscription renews with.

**Request**:

```json
{
    "requestInfo": {
        "requestReferenceId": "1c80bb86-f892-4b21-a919-1357811d6c4f"
    },
    "effective": "IMMEDIATELY",
    "items": [
        {  
           "currentSKU": "BASIC_TIER_1M",
           "SKU": "BASIC_PLAN_1M",
           "displayName": "Basic Plan"
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
                "SKU": "BASIC_TIER_1M",
                "displayName": "Basic Tier",                        
                "description": "Access to Game Stream",
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
                "SKU": "BASIC_PLAN_1M",
                "displayName": "Basic Plan",                        
                "description": "Access to Game Stream",
                "price": 9990
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

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v2/subscription/changeMetadata/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*: The transaction identifier of the auto-renewable subscription to get changes to its metadata. Use the subscription’s original transaction ID or any subsequent transaction ID of a transaction related to the subscription.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionChangeMetadataRequest`

The request body that contains the metadata changes.

## Responses

- `200` OK (`TransactionsResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(FamilyTransactionNotSupportedError | InvalidTransactionIdError | RepeatedRequestReferenceIdError | NullRequestInfoError | NullEffectiveError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | SKULengthExceededError | CurrentSKULengthExceededError | DescriptionLengthExceededError | DisplayNameLengthExceededError | InvalidSKUError | InvalidTaxProductCodeError | MismatchedStorefrontError | AtLeastOneOfDisplayNameOrDescriptionError | DuplicateSKUInRequestError | BundleItemsOnNonBundleParentError | NullItemsError | NullItemError | ProductAlreadyExistsError | MultipleOperationsOnSingleSKUError | ChangeItemNotFoundError | NullCurrentSKUError | InvalidOperationError | InvalidPartnerInfoError)`, `application/json`)
- `401` Unauthorized (`UnauthorizedError`, `application/json`): The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Authorizing API requests from your server](./authorizing-server-calls.md).
- `403` Forbidden (`(ForbiddenError | SubscriptionNotEligibleError | ChangeMetadataOfBundleItemNotAllowedError)`, `application/json`)
- `404` Not Found (`(NotFoundError | TransactionIdNotFoundError)`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md).
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Subscription metadata changes from the server
- [object SubscriptionChangeMetadataRequest](./subscriptionchangemetadatarequest.md)
  The request body you provide to change the metadata of a subscription.
- [object SubscriptionChangeMetadataResponse](./subscriptionchangemetadataresponse.md)
  The response body for a successful subscription metadata change.
- [object SubscriptionChangeMetadataDescriptors](./subscriptionchangemetadatadescriptors.md)
  The subscription metadata to change, specifically the description and display name.
- [object SubscriptionChangeMetadataItem](./subscriptionchangemetadataitem.md)
  The metadata to change for an item, specifically its SKU, description, and display name.
- [object ChangeMetadataBundleItem](./changemetadatabundleitem.md)
- [object SubscriptionChangeMetadataRequestV1](./subscriptionchangemetadatarequestv1.md)
- [object SubscriptionChangeMetadataItemV1](./subscriptionchangemetadataitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-metadata)*