# Sync the List of Courses

**Framework**: Device Management  
**Kind**: httpRequest

Get updates about the list of courses the server manages.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This sync service uses a cursor returned by the full course-roster service. It returns a list of all modifications (additions or deletions) made since the cursor date, for up to 7 days.

This service may return the same course more than once. You can identify duplicates by matching their `unique_identifier` values.

## Request Body

The object containing the request information.

## See Also

- [object BaseRosterCourse](baserostercourse.md)
  A base course’s properties and their values.
- [object RosterCourse](rostercourse.md)
  A course’s properties and their values.
- [Get the List of Courses](fetch-course-roster.md)
  Obtain a list of the courses the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/fetch-course-roster-sync)*