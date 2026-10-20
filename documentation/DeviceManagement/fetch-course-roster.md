# Get the List of Courses

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Obtain a list of the courses the server manages.

**Availability**:
- Device Assignment Services 5.0+

## Topics

### Response
- [object RosterCourseResponse](./rostercourseresponse.md)
  The response that contains a list of courses.

## Endpoint

`POST https://mdmenrollment.apple.com/roster/class/course`

## Request Body

**Content-Type**: `application/json`  
**Type**: `RosterRequest`

The object containing the request information.

## Responses

- `200` OK (`RosterCourseResponse`, `application/json`): The request was successful. The server returns a list of courses.
- `400` Bad Request: The server was unable to process the request.

## See Also

### Course management
- [object BaseRosterCourse](./baserostercourse.md)
  A base course’s properties and their values.
- [object RosterCourse](./rostercourse.md)
  A course’s properties and their values.
- [Sync the List of Courses](./fetch-course-roster-sync.md)
  Get updates about the list of courses the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-course-roster)*