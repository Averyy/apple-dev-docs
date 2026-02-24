# RosterCourseResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains a list of courses.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RosterCourseResponse
```

## Properties

- `courses` ([RosterCourse]): Provides information about courses, sorted in lexical order by a course `source_system_identifier`. The organization must provide this identifier to Apple.
- `cursor` (string): A hex string that should be used for the next request to paginate. This field data type has a maximum length of 512 UTF-8 characters.
- `more_to_follow` (boolean): Indicates whether the request’s limit and cursor values resulted in only a partial list of classes. If true, the MDM server should then make another request (starting from the newly returned cursor) to obtain additional records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rostercourseresponse)*