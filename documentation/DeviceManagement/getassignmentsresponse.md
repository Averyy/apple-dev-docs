# GetAssignmentsResponse

**Framework**: Device Management  
**Kind**: dictionary

The paginated response that contains requested assignments.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object GetAssignmentsResponse
```

## Mentions

- [Managing Apps and Books Through Web Services](managing-apps-and-books-through-web-services.md)
- [Managing Assets](managing-assets.md)

## Topics

### Objects and Data Types
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.

## Properties

- `assignments` ([Assignment]): The list of  requested assignments.
- `currentPageIndex` (int32): The current page index of the paginated response.
- `nextPageIndex` (int32): The next page index in the paginated response. The response only includes this field when  there is a next page.
- `size` (int32): The number of assignments on the current page.
- `totalPages` (int32): The total number of pages in the paginated response.
- `versionId` (string): The current version identifier. When traversing the paginated response, use `versionId` to identify when changes occur to underlying data. When any writes occur to the underlying data in a fetch, `versionId` updates.
- `mdmInfo` (MdmInfo): The current information for the provided token. The response only includes this field when MDM sets a value using the [`Client Config`](client-config-4szk1.md) endpoint.
- `tokenExpirationDate` (string): The token expiration date in an ISO-8601 format. Note: The server shows all dates and times in UTC.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates and avoid double-counting records when different content managers upload duplicate tokens.

## See Also

- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/getassignmentsresponse)*