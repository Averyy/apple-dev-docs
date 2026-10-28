# Sync the Locations

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get updates about the list of locations the server manages.

**Availability**:
- Device Assignment Services 5.0+

## Discussion

This sync service uses a cursor returned by the full location-roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, up to 7 days.

This service may return the same location more than once. You can identify duplicates by matching their `unique_identifier` values.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class/location/sync`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RosterRequest`

The object containing the request information.

## Responses

- `200` OK (`RosterClassLocationResponse`, `application/json`): The request was successful. The server returns a list of locations.
- `400` Bad Request: The server was unable to process the request.

## See Also

### Location management
- [object BaseRosterLocation](./baserosterlocation.md)
  A base location’s properties and their values.
- [object RosterLocation](./rosterlocation.md)
  A location’s properties and their values.
- [Get the List of Locations](./fetch-location-roster.md)
  Obtain a list of the locations the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-location-roster-sync)*