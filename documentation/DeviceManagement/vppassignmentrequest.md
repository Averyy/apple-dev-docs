# VppAssignmentRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for a list of assignments.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object VppAssignmentRequest
```

## Properties

- `adamIdStr` (string): The unique identifier for a product in the iTunes Store.
- `clientUserIdStr` (string): If specified, returns only assignments assigned to the given client user ID.
- `pageIndex` (int32): The index of the page to lookup. To page through the assignemnts, use the `nextPageIndex` value returned in the previous [`VppAssignmentsResponse`](vppassignmentsresponse.md). This must be used in combination with a `requestID`, also from the previous response.
- `requestId` (string): A unique ID that is used when making paginated requests.
- `serialNumber` (string): If specified, returns only assignments assigned to the given serial number.
- `sToken` (string) *(required)*: The authentication token.

## See Also

- [object VppAssignmentsResponse](vppassignmentsresponse.md)
  The response that contains a list of assignments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppassignmentrequest)*