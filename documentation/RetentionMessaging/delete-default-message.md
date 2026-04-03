# Delete Default Message

**Framework**: Retention Messaging API  
**Kind**: httpRequest

Deletes a default message for a product in a locale.

**Availability**:
- Retention Messaging API 1.0+

## Mentions

- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

Call this endpoint to delete a default message configuration. After a successful deletion, `productId` in `locale` has no default message.

This endpoint is idempotent. If the product has no configured default message for the locale, the endpoint still responds with a `200` status code.

## Endpoint

`DELETE https://api.storekit-sandbox.itunes.apple.com/inApps/v1/messaging/default/{productId}/{locale}`

## Parameters

- `locale` (locale) *(required)*: The locale of the default message configuration.
- `productId` (productId) *(required)*: The product ID of the default message configuration.

## See Also

- [Configure Default Message](configure-default-message.md)
  Configures a default message for a specific product in a specific locale.
- [Get Default Message](get-default-message.md)
  Gets the default message for a specific product in a specific locale, if it’s configured.
- [object DefaultConfigurationRequest](defaultconfigurationrequest.md)
  The request body that contains the default configuration information.
- [object DefaultConfigurationResponse](defaultconfigurationresponse.md)
  The response body that contains the default configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/delete-default-message)*