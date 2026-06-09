# Sync the List of Classes

**Framework**: Device Management  
**Kind**: httpRequest

Get updates about the list of classes the server manages.

**Availability**:
- Device Assignment Services 5.0+

#### Discussion

This sync service uses a cursor that is returned by the full class-roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, for up to 7 days.

This service may return the same class more than once. You can identify duplicates by matching their `unique_identifier` values.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class/sync`

## Request Body

The object containing the request information.

## See Also

- [object RosterClass](rosterclass.md)
  A class’s properties and their values.
- [Get the List of Classes](fetch-class-roster.md)
  Obtain a list of classes the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-class-roster-sync)*