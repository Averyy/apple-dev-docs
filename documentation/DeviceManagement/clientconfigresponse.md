# ClientConfigResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains the client configuration.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object ClientConfigResponse
```

#### Discussion

Client config should be checked regularly in order to verify expected values for the various fields.

## Topics

### Content Metadata
- [Apps and books metadata for organizations](apps-and-books-metadata-for-organizations.md)
  Get metadata for apps and books your organization owns.

## Properties

- `countryISO2ACode` (string): The ISO alpha-2 country code that designates the organization’s location.
- `defaultPlatform` (string): The value that the MDM client passes for the platform parameter in the `contentMetadataLookup` request. For more information about how the MDM client queries metadata by using `contentMetadataLookup`, see [`Getting app and book information (Legacy)`](getting-app-and-book-information-legacy.md).
- `notificationUrl` (string): The current URL to post notifications to.
- `subscribedNotificationTypes` ([string]): The set of currently subscribed notification types.
- `websiteURL` (string): The current website URL for the specified platform.
- `mdmInfo` (MdmInfo): The current information for the provided token. The response only includes this field when the MDM client sets a value using the [`Client Config`](client-config-4szk1.md) endpoint.
- `notificationAuthToken` (string): The current shared secret that the server returns in the Authorization header of notifications.
- `tokenExpirationDate` (string): The token’s expiration date in an ISO-8601 format. Note: The server shows all dates and times in UTC.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates and avoid double-counting records when different content managers upload duplicate tokens.
- `locationName` (string): The current name of the library.

## See Also

- [object ClientConfigRequest](clientconfigrequest.md)
  The request for the client configuration.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/clientconfigresponse)*