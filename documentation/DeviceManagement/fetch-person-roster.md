# Get the List of People

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Obtain a list of people the server manages, across the organization.

**Availability**:
- Device Assignment Services 5.0+

## Discussion

In addition to instructors and students, this list may contain additional people who don’t belong to any class.

## Topics

### Response
- [object RosterPersonResponse](./rosterpersonresponse.md)
  The response that contains the people in the organization.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class/person`

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
- [Sync the List of People](./fetch-person-roster-sync.md)
  Get updates about the list of people the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-person-roster)*