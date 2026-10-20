# Get the List of Classes

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Obtain a list of classes the server manages.

**Availability**:
- Device Assignment Services 5.0+

## Topics

### Request and Response
- [object RosterRequest](./rosterrequest.md)
  The request for a list of classes.
- [object RosterClassResponse](./rosterclassresponse.md)
  The response that contains a list of classes.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RosterRequest`

The object containing the request information.

## Responses

- `200` OK (`RosterClassResponse`, `application/json`): The request was successful. The server returns a list of classes.
- `400` Bad Request: The server was unable to process the request.

## See Also

### Class management
- [object RosterClass](./rosterclass.md)
  A class’s properties and their values.
- [Sync the List of Classes](./fetch-class-roster-sync.md)
  Get updates about the list of classes the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-class-roster)*