# Delete Default Message

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Deletes a default message for a product in a locale.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)

#### Discussion

Call this endpoint to delete a default message configuration. After a successful deletion, `productId` in `locale` has no default message.

This endpoint is idempotent. If the product has no configured default message for the locale, the endpoint still responds with a `200` status code.

## Endpoint

`DELETE https://api.storekit-sandbox.apple.com/inApps/v1/messaging/default/{productId}/{locale}`

## Parameters

### Path Parameters

- `locale` (locale) *(required)*: The locale of the default message configuration.
- `productId` (productId) *(required)*: The product ID of the default message configuration.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request (`(InvalidProductIdError | InvalidLocaleError)`, `application/json`): The request is invalid and unacceptable.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Default message configuration
- [Configure Default Message](./configure-default-message.md)
  Configures a default message for a specific product in a specific locale.
- [Get Default Message](./get-default-message.md)
  Gets the default message for a specific product in a specific locale, if it’s configured.
- [object DefaultConfigurationRequest](./defaultconfigurationrequest.md)
  The request body that contains the default configuration information.
- [object DefaultConfigurationResponse](./defaultconfigurationresponse.md)
  The response body that contains the default configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/delete-default-message)*