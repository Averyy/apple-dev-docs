# Migrate a Subscription to Advanced Commerce API

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Migrate a subscription that a customer purchased through Apple In-App Purchase to a subscription you manage using the Advanced Commerce API.

**Availability**:
- Advanced Commerce API 1.3+

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Authorizing API requests from your server](./authorizing-server-calls.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)
- [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md)

## Discussion

> **Note**: You can use the Advanced Commerce API and the StoreKit [Apple In-App Purchase](../StoreKit/in-app-purchase.md) APIs in the same app. Both APIs use the App Store commerce system, including the same signed JWS transactions and JWS renewal info. For products that you offer using the Apple In-App Purchase API, you set up product identifiers in App Store Connect. For products that you offer using the Advanced Commerce API, you host and manage your own catalog of SKUs and add product details dynamically at runtime.

### Example request

```json
{
  "requestInfo": {
        "requestReferenceId": "1c80bb86-f892-4b21-a919-1357811d6c4f"
    },
  "targetProductId": "com.example.genericsku",
  "targetAppAppleId": 120398,            
  "taxCode": "C003-00-1",
  "items": [
    {
     "SKU": "ANNES_GOLD_TIER_1M",
     "displayName": "Gold Tier",                        
     "description": "Access to Anne's Game Stream"
    }
  ]
}
```

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v2/subscription/migrate/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*: The transaction identifier of the auto-renewable subscription to migrate. Use the subscription’s original transaction ID or any subsequent transaction ID of a transaction related to the subscription.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionMigrateRequest`

The request body that contains the details for the migration.

## Responses

- `200` OK (`TransactionsResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(RepeatedRequestReferenceIdError | NullRequestInfoError | NullTaxCodeError | NullItemsError | NullSKUError | NullDisplayNameError | NullDescriptionError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | SKULengthExceededError | DescriptionLengthExceededError | DisplayNameLengthExceededError | InvalidProductError | InvalidSKUError | InvalidTaxProductCodeError | MismatchedStorefrontError | MissingPricingConfigForStorefrontError | AtLeastOneItemError | NullTargetProductIDError | InvalidTargetProductIDError | SubscriptionAlreadyMigratedError | ItemLimitExceededError | InvalidTransactionIdError | AppTransactionIdNotSupportedError | FamilyTransactionNotSupportedError | InvalidAssignedTransactionNotSupportedError | BundleTransactionIdNotSupportedError | NullItemError | InvalidPartnerInfoError | TooFewBundleItemsError | TooManyBundleItemsError | BundleMigrateSkuMismatchError | BundleMigrateNotSupportedError | DuplicateSKUInRequestError | NegativePriceError)`, `application/json`)
- `401` Unauthorized (`UnauthorizedError`, `application/json`): The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Authorizing API requests from your server](./authorizing-server-calls.md).
- `403` Forbidden (`(ForbiddenError | SubscriptionDoesNotExistError | SubscriptionAlreadyExistsError | SubscriptionNotEligibleError | ProductNotOwnedError | InactiveACASubError | ProductNotEligibleError | StorefrontChangeError | MigrationNotAllowedWhenPriceIncreaseCommunicatedError)`, `application/json`)
- `404` Not Found (`(NotFoundError | TransactionIdNotFoundError | ProductNotFoundError)`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md).
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`): Server error. Try again later.

## See Also

### Migration from the server
- [object SubscriptionMigrateRequest](./subscriptionmigraterequest.md)
  The subscription details you provide to migrate a subscription from Apple In-App Purchase to the Advanced Commerce API, such as descriptors, items, storefront, and more.
- [object SubscriptionMigrateResponse](./subscriptionmigrateresponse.md)
  A response that contains signed renewal and transaction information after a subscription successfully migrates to the Advanced Commerce API.
- [object SubscriptionMigrateItem](./subscriptionmigrateitem.md)
  The SKU, description, and display name to use for a migrated subscription item.
- [object MigrateBundleItem](./migratebundleitem.md)
- [object SubscriptionMigrateRenewalItem](./subscriptionmigraterenewalitem.md)
  The item information that replaces a migrated subscription item when the subscription renews.
- [object SubscriptionMigrateDescriptors](./subscriptionmigratedescriptors.md)
  The description and display name of the subscription to migrate to that you manage.
- [object SubscriptionMigrateRequestV1](./subscriptionmigraterequestv1.md)
- [object SubscriptionMigrateItemV1](./subscriptionmigrateitemv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/migrate-subscription-to-advanced-commerce-api)*