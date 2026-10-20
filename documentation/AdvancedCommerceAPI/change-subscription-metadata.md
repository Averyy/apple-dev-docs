# Change Subscription Metadata

**Framework**: Advanced Commerce API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the SKU, display name, and description associated with a subscription, without affecting the subscription’s billing or its service.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Authorizing API requests from your server](./authorizing-server-calls.md)
- [Advanced Commerce API changelog](./changelog.md)
- [Identifying rate limits for Advanced Commerce APIs](./ratelimits.md)

#### Discussion

Use this endpoint to update the display name and description of an auto-renewable subscription. Calling this endpoint doesn’t change the price, billing details, or the service. For example, you can call `Change Subscription Metadata` if a subscription’s display name changes due to a change in its branding.

Don’t call this endpoint if a customer is changing subscriptions to receive a different service, such as upgrading, downgrading, or cross-grading. For such changes, use [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md).

## Endpoint

`POST https://api.storekit-sandbox.apple.com/advancedCommerce/v1/subscription/changeMetadata/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (string) *(required)*: The transaction identifier of the auto-renewable subscription to get changes to its metadata. Use the subscription’s original transaction ID or any subsequent transaction ID of a transaction related to the subscription.

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionChangeMetadataRequest`

The request body that contains the metadata changes.

## Responses

- `200` OK (`SubscriptionChangeMetadataResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(RepeatedRequestReferenceIdError | NullRequestInfoError | NullEffectiveError | InvalidAppAccountTokenError | NullRequestReferenceIDError | InvalidRequestReferenceIDError | InvalidConsistencyTokenError | InvalidStorefrontError | SKULengthExceededError | DescriptionLengthExceededError | DisplayNameLengthExceededError | InvalidProductChangesError | InvalidDisplayNameError | InvalidDescriptionError | InvalidProductError | InvalidSKUError | InvalidTaxProductCodeError | MismatchedStorefrontError | MismatchedStorefrontError | OperationNotAllowedError | MalformedPayloadError | AtLeastOneItemError | AtLeastOneOfDisplayNameOrDescriptionError)`, `application/json`)
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Authorizing API requests from your server](./authorizing-server-calls.md).
- `403` Forbidden (`(SubscriptionDoesNotExistError | SubscriptionNotEligibleError | ProductNotOwnedError | InactiveACASubError | ProductNotEligibleError)`, `application/json`)
- `404` Not Found (`(TransactionIdNotFoundError | ProductNotFoundError)`, `application/json`)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-metadata)*