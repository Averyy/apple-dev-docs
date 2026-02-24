# RosterCourse

**Framework**: Device Management  
**Kind**: dictionary

A course’s properties and their values.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RosterCourse
```

## Properties

- `course_number` (string): The number of the course.
- `name` (string): The course name. Maximum length 1024 UTF-8 characters.
- `source` (string): The data source where the class was created.
- `source_system_identifier` (string): The identifier configured by organization for the course. Maximum length is 256 UTF-8 characters. Value can be null.
- `unique_identifier` (string): The unique identifier for the course. Maximum length 256 UTF-8 characters.
- `op_date` (string): The time stamp, in iSO 8601 format, when the course was added, updated, or deleted.
- `status` (string): The status for the course.

## See Also

- [object BaseRosterCourse](baserostercourse.md)
  A base course’s properties and their values.
- [Get the List of Courses](fetch-course-roster.md)
  Obtain a list of the courses the server manages.
- [Sync the List of Courses](fetch-course-roster-sync.md)
  Get updates about the list of courses the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rostercourse)*