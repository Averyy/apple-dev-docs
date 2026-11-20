# Change Subscription Metadata V1

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Advanced Commerce API 1.0+

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v1/subscription/changeMetadata/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionChangeMetadataRequestV1`

## Responses

- `200` OK (`SubscriptionChangeMetadataResponse`, `application/json`)
- `400` Bad Request (`(RepeatedRequestReferenceIdError | NullRequestInfoError | NullEffectiveError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | SKULengthExceededError | DescriptionLengthExceededError | DisplayNameLengthExceededError | InvalidProductChangesError | InvalidDisplayNameError | InvalidDescriptionError | InvalidProductError | InvalidSKUError | InvalidTaxProductCodeError | MismatchedStorefrontError | OperationNotAllowedError | MalformedPayloadError | AtLeastOneItemError | AtLeastOneOfDisplayNameOrDescriptionError | InvalidPartnerInfoError)`, `application/json`)
- `401` Unauthorized
- `403` Forbidden (`(SubscriptionDoesNotExistError | SubscriptionNotEligibleError | ProductNotOwnedError | InactiveACASubError | ProductNotEligibleError)`, `application/json`)
- `404` Not Found (`(TransactionIdNotFoundError | ProductNotFoundError)`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`)
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-metadata-v1)*