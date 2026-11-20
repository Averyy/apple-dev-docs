# Change Subscription Price V1

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- Advanced Commerce API 1.0+

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v1/subscription/changePrice/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionPriceChangeRequestV1`

## Responses

- `200` OK (`SubscriptionPriceChangeResponse`, `application/json`)
- `400` Bad Request (`(NullRequestInfoError | NullItemsError | NullSKUError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | InvalidCurrencyError | NegativePriceError | SKULengthExceededError | DescriptionLengthExceededError | DisplayNameLengthExceededError | InvalidProductError | InvalidSKUError | MismatchedStorefrontError | MissingPricingConfigForStorefrontError | OperationNotAllowedError | MalformedPayloadError | DependentSKUsCannotBeSharedError | DependentSKUsCannotBeChainedError | ItemCannotBeSpecifiedMultipleTimesError | PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError | InvalidSKUProvidedMustBeCurrentSKUSetToRenewError | NullPriceError | InvalidOperationError | TooManySeatPriceTiersError | InvalidMaximumSeatQuantityError | SeatPriceTiersNotDecreasingError | SeatPriceTiersNotAllowedForBundleError | PriceNotAllowedWithSeatPriceTiersError | SeatPriceTiersRequiredError | SubsForGroupsRequiresLatestVersionError)`, `application/json`)
- `401` Unauthorized
- `403` Forbidden (`(SubscriptionDoesNotExistError | SubscriptionNotEligibleError)`, `application/json`)
- `404` Not Found (`TransactionIdNotFoundError`, `application/json`)
- `429` (`RateLimitExceededError`, `application/json`)
- `500` Internal Server Error (`(GeneralInternalError | GeneralInternalRetryableError)`, `application/json`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-price-v1)*