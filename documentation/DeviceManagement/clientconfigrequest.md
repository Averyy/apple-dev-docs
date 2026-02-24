# ClientConfigRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for the client configuration.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ClientConfigRequest
```

## Mentions

- [Subscribing to Notifications](subscribing-to-notifications.md)
- [Upgrading to the new App and Book Management API](upgrading-to-the-new-app-and-book-management-api.md)

## Topics

### Objects and Data Types
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.

## Properties

- `notificationTypes` ([string]): The complete set of notification types to which MDM subscribes.
- `notificationUrl` (string): The URL to which subscribed notifications POST. This URL should only include a host and path.
- `mdmInfo` (MdmInfo): This value is returned by the server on all subsequent responses, and MDM uses it to ensure that no other MDM manages the same organization.
- `notificationAuthToken` (string): The bearer token that the server provides in the Authorization header of notifications. This is a shared secret between you and the server to verify that incoming notifications are from Apple.

## See Also

- [object ClientConfigResponse](clientconfigresponse.md)
  The response that contains the client configuration.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clientconfigrequest)*