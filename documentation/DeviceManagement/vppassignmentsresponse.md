# VppAssignmentsResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains a list of assignments.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object VppAssignmentsResponse
```

## Properties

- `assignments` ([VppAssignment]): An array of dictionaries representing the current assignments.
- `assignmentsInCurrentPage` (int32): The total number of assignments in the current page.
- `clientContext` (string): The value currently associated with the provided `sToken`. This field is only included in the response when a value has been set via the [`Client Configuration`](client-configuration.md) endpoint. See [`Protecting Your VPP Account`](protecting-your-vpp-account.md) for more information.
- `currentPageIndex` (int32): The index of the page being returned.
- `expirationMillis` (int64): The UNIX epoch timestamp, in milliseconds, when the account’s `sToken` or password expires (whichever is earlier).
- `location` (VppLocation): The location associated with the provided `sToken`. This field is only returned when a location token is used with an Apple School Manager account.
- `nextPageIndex` (int32): The index of the next assignments page. This field will only be returned if there are additional assignments pages to read.
- `requestId` (string): The ID to be used for subsequent assignments page lookups. This field will only be returned if there are greater than 300 assignments.
- `status` (int32): The status code for the response. Possible values are: `0` = Success. `-1` = Failure.
- `totalAssignments` (int32): The total number of assignments for the provided criteria.
- `totalPages` (int32): The total number of pages of assignments. There will be 300 assignments per page.
- `getuId` (string)

## See Also

- [object VppAssignmentRequest](vppassignmentrequest.md)
  The request for a list of assignments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppassignmentsresponse)*