# Sync the List of Classes

**Framework**: Device Management  
**Kind**: httpRequest

Get updates about the list of classes the server manages.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This sync service uses a cursor that is returned by the full class-roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, for up to 7 days.

This service may return the same class more than once. You can identify duplicates by matching their `unique_identifier` values.

## Request Body

The object containing the request information.

## See Also

- [object RosterClass](rosterclass.md)
  A class’s properties and their values.
- [Get the List of Classes](fetch-class-roster.md)
  Obtain a list of classes the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-class-roster-sync)*