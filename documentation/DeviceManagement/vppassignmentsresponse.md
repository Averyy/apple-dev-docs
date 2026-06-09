# VppAssignmentsResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains a list of assignments.

**Availability**:
- VPP License Management 1.1+

## Declaration

```swift
object VppAssignmentsResponse
```

## Properties

- `assignments` ([VppAssignment]): An array of dictionaries representing the current assignments.
- `assignmentsInCurrentPage` (int32): The total number of assignments in the current page.
- `clientContext` (string): The value currently associated with the provided `sToken`. This field is only included in the response when a value is set with the [`Client Configuration`](client-configuration.md) endpoint.
- `currentPageIndex` (int32): The index of the page being returned.
- `expirationMillis` (int64): The UNIX epoch timestamp, in milliseconds, when the account’s `sToken` or password expires (whichever is earlier).
- `location` (VppLocation): The location associated with the provided `sToken`. This field only returns when using a location token with an Apple School Manager account.
- `nextPageIndex` (int32): The index of the next assignments page. This field only returns when there are additional assignments pages to read.
- `requestId` (string): The ID to use for subsequent assignments page lookups. This field only returns when there are more than 300 assignments.
- `status` (int32): The status code for the response. Possible values are: `0` = Success. `-1` = Failure.
- `totalAssignments` (int32): The total number of assignments for the provided criteria.
- `totalPages` (int32): The total number of pages of assignments. There will be 300 assignments per page.
- `getuId` (string)

## See Also

- [object VppAssignmentRequest](vppassignmentrequest.md)
  The request for a list of assignments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vppassignmentsresponse)*