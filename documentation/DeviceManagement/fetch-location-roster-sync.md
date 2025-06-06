# Sync the Locations

**Framework**: Device Management  
**Kind**: httpRequest

Get updates about the list of locations the server manages.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This sync service uses a cursor returned by the full location-roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, up to 7 days.

This service may return the same location more than once. You can identify duplicates by matching their `unique_identifier` values.

## Request Body

The object containing the request information.

## See Also

- [object BaseRosterLocation](baserosterlocation.md)
  A base location’s properties and their values.
- [object RosterLocation](rosterlocation.md)
  A location’s properties and their values.
- [Get the List of Locations](fetch-location-roster.md)
  Obtain a list of the locations the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-location-roster-sync)*