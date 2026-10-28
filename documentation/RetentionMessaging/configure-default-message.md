# Configure Default Message

**Framework**: Retention Messaging API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Configures a default message for a specific product in a specific locale.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](./identifying-rate-limits.md)
- [Setting up retention messages](./setting-up-retention-messages.md)

## Discussion

When this request succeeds, the system configures the retention message you specify in the request body as the default message for `productId` in `locale`. You can configure a default message for every auto-renewable subscription’s product ID in every locale for your app.

You can configure only text-based messages and text-based messages with an image as a default message. Call [`Get Message List`](./get-message-list.md) and [`Get Image List`](./get-image-list.md) to check the current state of messages and images, respectively.

> **Note**: If either the message or the image isn’t in an `APPROVED` state, the request fails with an error.

To replace a default message, call this endpoint again with a different message identifier. This endpoint is idempotent. If the product already has a default message for the locale, the endpoint overwrites that configuration and responds with a `200` status code.

To delete a default message, call [`Delete Default Message`](./delete-default-message.md).

### Use default messages

Configure a default message for each product in each locale. If you implement the `Get Retention Message` endpoint, the system requires a default message for every product in each locale where you provide real-time retention messages. For more information, see [Setting up your Get Retention Message endpoint](./setting-up-retention-messaging-endpoint.md).

The system uses the default messages if your server response fails for any reason, or if you don’t implement the `Get Retention Message` endpoint.

To present promotional-offer or switch-plan retention messages instead of default messages, implement the `Get Retention Message` endpoint to respond with those message types in real time. For more information, see [Setting up your Get Retention Message endpoint](./setting-up-retention-messaging-endpoint.md).

## Endpoint

`PUT https://api.storekit-sandbox.apple.com/inApps/v1/messaging/default/{productId}/{locale}`

## Parameters

### Path Parameters

- `locale` (locale) *(required)*: The locale for the default configuration.
- `productId` (productId) *(required)*: The product identifier for the default configuration.

## Request Body

**Content-Type**: `application/json`  
**Type**: `DefaultConfigurationRequest`

The request body that includes the message identifier to configure as the default message.

## Responses

- `200` OK: Request succeeded.
- `400` Bad Request (`(InvalidProductIdError | InvalidLocaleError)`, `application/json`): The request is invalid and unacceptable.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md).
- `403` Forbidden (`(MessageNotApprovedError | ImageNotApprovedError)`, `application/json`): The provided message or image isn’t in an approved state, so you can’t configure it as a default message.
- `404` Not Found (`MessageNotFoundError`, `application/json`): The system can’t find the message.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Default message configuration
- [Get Default Message](./get-default-message.md)
  Gets the default message for a specific product in a specific locale, if it’s configured.
- [Delete Default Message](./delete-default-message.md)
  Deletes a default message for a product in a locale.
- [object DefaultConfigurationRequest](./defaultconfigurationrequest.md)
  The request body that contains the default configuration information.
- [object DefaultConfigurationResponse](./defaultconfigurationresponse.md)
  The response body that contains the default configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/configure-default-message)*