# VppClientConfigRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for the client configuration.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object VppClientConfigRequest
```

## Properties

- `clientContext` (string): Any JSON string under 256 bytes. The server stores the value of this field, and this value is returned in all responses. To clear the field’s value, provide an empty string as the input value (””). See [`Protecting Your VPP Account`](protecting-your-vpp-account.md) for more information.
- `notificationToken` (string): The token to use when sending notifications through `notificationURL`.
- `sToken` (string) *(required)*: The authentication token. For more information, see [`Authentication`](managing-apps-and-books-through-web-services-legacy#Authentication.md).

## See Also

- [object VppClientConfigResponse](vppclientconfigresponse.md)
  The response that contains the client configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppclientconfigrequest)*