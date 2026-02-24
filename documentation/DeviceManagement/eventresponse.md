# EventResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains the event identifier.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object EventResponse
```

## Mentions

- [Managing Assets](managing-assets.md)
- [Managing Users](managing-users.md)

## Topics

### Objects and Data Types
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.

## Properties

- `eventId` (string): The unique identifier for the asynchronous event.
- `mdmInfo` (MdmInfo): The current information for the provided token. The response only includes this field when MDM sets a value using the [`Client Config`](client-config-4szk1.md) endpoint.
- `tokenExpirationDate` (string): The token expiration date in an ISO-8601 format. Note: The server shows all dates and times in UTC.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates and avoid double-counting records when different content managers upload duplicate tokens.

## See Also

- [object ManageAssetsRequest](manageassetsrequest.md)
  The request for asset management.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/eventresponse)*