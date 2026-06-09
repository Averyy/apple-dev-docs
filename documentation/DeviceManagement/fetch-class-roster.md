# Get the List of Classes

**Framework**: Device Management  
**Kind**: httpRequest

Obtain a list of classes the server manages.

**Availability**:
- Device Assignment Services 5.0+

## Topics

### Request and Response
- [object RosterRequest](rosterrequest.md)
  The request for a list of classes.
- [object RosterClassResponse](rosterclassresponse.md)
  The response that contains a list of classes.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class`

## Request Body

The object containing the request information.

## See Also

- [object RosterClass](rosterclass.md)
  A class’s properties and their values.
- [Sync the List of Classes](fetch-class-roster-sync.md)
  Get updates about the list of classes the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-class-roster)*