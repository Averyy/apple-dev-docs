# DefaultConfigurationResponse

**Framework**: Retention Messaging API  
**Kind**: dictionary

The response body that contains the default configuration information.

**Availability**:
- Retention Messaging API 1.4+

## Declaration

```swift
object DefaultConfigurationResponse
```

#### Discussion

This is the response body for the [`Get Default Message`](get-default-message.md) endpoint.

## Properties

- `messageIdentifier` (messageIdentifier) *(required)*: The message identifier of the retention message you configured as a default.

## See Also

- [Configure Default Message](configure-default-message.md)
  Configures a default message for a specific product in a specific locale.
- [Get Default Message](get-default-message.md)
  Gets the default message for a specific product in a specific locale, if it’s configured.
- [Delete Default Message](delete-default-message.md)
  Deletes a default message for a product in a locale.
- [object DefaultConfigurationRequest](defaultconfigurationrequest.md)
  The request body that contains the default configuration information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/defaultconfigurationresponse)*