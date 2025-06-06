# Sync the List of People

**Framework**: Device Management  
**Kind**: httpRequest

Get updates about the list of people the server manages.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This sync service uses a cursor returned by the full person-roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, for up to 7 days.

This service may return the same person more than once. You can identify duplicates by matching their `unique_identifier` values.

## Request Body

The object containing the request information.

## See Also

- [object RosterPerson](rosterperson.md)
  A person’s properties and their values.
- [Get the List of People](fetch-person-roster.md)
  Obtain a list of people the server manages, across the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-person-roster-sync)*