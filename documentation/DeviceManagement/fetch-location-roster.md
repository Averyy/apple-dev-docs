# Get the List of Locations

**Framework**: Device Management  
**Kind**: httpRequest

Obtain a list of the locations the server manages.

**Availability**:
- Device Assignment Services 5.0+

## Topics

### Response
- [object RosterClassLocationResponse](rosterclasslocationresponse.md)
  The response that contains a list of locations.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class/location`

## Request Body

The object containing the request information.

## See Also

- [object BaseRosterLocation](baserosterlocation.md)
  A base location’s properties and their values.
- [object RosterLocation](rosterlocation.md)
  A location’s properties and their values.
- [Sync the Locations](fetch-location-roster-sync.md)
  Get updates about the list of locations the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-location-roster)*