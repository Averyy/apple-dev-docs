# VppClientConfigRequest

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

The request for the client configuration.

**Availability**:
- VPP License Management 1.0+

## Declaration

```
object VppClientConfigRequest
```

## Properties

- `clientContext` (string): Any JSON string under 256 bytes. The server stores the value of this field, and this value returns in all responses. To clear the field’s value, provide an empty string as the input value (””).
- `notificationToken` (string): The token to use when sending notifications through `notificationURL`.
- `sToken` (string) *(required)*: The authentication token. For more information, see [Authenticate with the web service](./managing-apps-and-books-through-web-services-legacy.md#Authenticate-with-the-web-service).

## See Also

### Request and Response
- [object VppClientConfigResponse](./vppclientconfigresponse.md)
  The response that contains the client configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppclientconfigrequest)*