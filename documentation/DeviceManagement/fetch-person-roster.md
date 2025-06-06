# Get the List of People

**Framework**: Device Management  
**Kind**: httpRequest

Obtain a list of people the server manages, across the organization.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

In addition to instructors and students, this list may contain additional people who don’t belong to any class.

## Topics

### Response
- [object RosterPersonResponse](rosterpersonresponse.md)
  The response that contains the people in the organization.

## Request Body

The object containing the request information.

## See Also

- [object RosterPerson](rosterperson.md)
  A person’s properties and their values.
- [Sync the List of People](fetch-person-roster-sync.md)
  Get updates about the list of people the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-person-roster)*