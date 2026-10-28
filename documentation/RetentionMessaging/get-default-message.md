# Get Default Message

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Gets the default message for a specific product in a specific locale, if it’s configured.

**Availability**:
- Retention Messaging API 1.4+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)
- [Retention Messaging API changelog](./retention-messaging-changelog.md)
- [Setting up retention messages](./setting-up-retention-messages.md)

## Discussion

Call this endpoint to retrieve the default message you previously configured for a specific product in a specific locale. If a default message isn’t configured, the endpoint returns an `HTTP 404` error with [`DefaultMessageNotFoundError`](./defaultmessagenotfounderror.md).

For information about setting up default messages, see [Setting up retention messages](./setting-up-retention-messages.md).

## Endpoint

`GET https://api.storekit-sandbox.apple.com/inApps/v1/messaging/default/{productId}/{locale}`

## Parameters

### Path Parameters

- `locale` (locale) *(required)*: The locale of the message.
- `productId` (productId) *(required)*: The product identifier of the message.

## Responses

- `200` OK (`DefaultConfigurationResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`(InvalidProductIdError | InvalidLocaleError)`, `application/json`): The request is invalid and unacceptable.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`DefaultMessageNotFoundError`, `application/json`): The default message for the specified product ID and locale wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Default message configuration
- [Configure Default Message](./configure-default-message.md)
  Configures a default message for a specific product in a specific locale.
- [Delete Default Message](./delete-default-message.md)
  Deletes a default message for a product in a locale.
- [object DefaultConfigurationRequest](./defaultconfigurationrequest.md)
  The request body that contains the default configuration information.
- [object DefaultConfigurationResponse](./defaultconfigurationresponse.md)
  The response body that contains the default configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/get-default-message)*