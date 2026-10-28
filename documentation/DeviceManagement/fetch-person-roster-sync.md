# Sync the List of People

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get updates about the list of people the server manages.

**Availability**:
- Device Assignment Services 5.0+

## Discussion

This sync service uses a cursor returned by the full person-roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, for up to 7 days.

This service may return the same person more than once. You can identify duplicates by matching their `unique_identifier` values.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class/person/sync`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RosterRequest`

The object containing the request information.

## Responses

- `200` OK (`RosterPersonResponse`, `application/json`): The request was successful. The server returns a list of people.
- `400` Bad Request: The server was unable to process the request.

## See Also

### People management
- [object RosterPerson](./rosterperson.md)
  A person’s properties and their values.
- [Get the List of People](./fetch-person-roster.md)
  Obtain a list of people the server manages, across the organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-person-roster-sync)*