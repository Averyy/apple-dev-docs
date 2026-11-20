# Migrate Subscription to Advanced Commerce API V1

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Advanced Commerce API 1.0+

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v1/subscription/migrate/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionMigrateRequestV1`

## Responses

- `200` OK (`SubscriptionMigrateResponse`, `application/json`)
- `400` Bad Request (`(RepeatedRequestReferenceIdError | NullRequestInfoError | NullTaxCodeError | NullItemsError | NullDescriptorsError | NullSKUError | NullDisplayNameError | NullDescriptionError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | SKULengthExceededError | DescriptionLengthExceededError | DisplayNameLengthExceededError | InvalidDisplayNameError | InvalidDescriptionError | InvalidProductError | InvalidSKUError | InvalidTaxProductCodeError | MismatchedStorefrontError | MissingPricingConfigForStorefrontError | OperationNotAllowedError | MalformedPayloadError | AtLeastOneItemError | NullTargetProductIDError | InvalidTargetProductIDError | SubscriptionAlreadyMigratedError | ItemLimitExceededError | PendingChangesMismatchError | AppTransactionIdNotSupportedError | FamilyTransactionNotSupportedError | InvalidAssignedTransactionNotSupportedError | SubsForGroupsRequiresLatestVersionError | InvalidPartnerInfoError)`, `application/json`)
- `401` Unauthorized
- `403` Forbidden (`(SubscriptionDoesNotExistError | SubscriptionAlreadyExistsError | SubscriptionNotEligibleError | ProductNotOwnedError | InactiveACASubError | ProductNotEligibleError | StorefrontChangeError | MigrationNotAllowedWhenPriceIncreaseCommunicatedError)`, `application/json`)
- `404` Not Found (`(TransactionIdNotFoundError | ProductNotFoundError)`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`)
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/migrate-subscription-to-advanced-commerce-api-v1)*