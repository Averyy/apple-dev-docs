# RosterClass

**Framework**: Device Management  
**Kind**: dictionary

A class’s properties and their values.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RosterClass
```

## Properties

- `class_display_name` (string): The Class Nickname in Apple School Manager. This name appears in the Schoolwork app and is modifiable by teachers within Schoolwork or by admins within Apple School Manager. Use this field for Classroom and Shared iPad class configurations. Available in X-Protocol Version 5 and later.
- `class_icon_identifier` (string): The class icon selected by teachers when they create or update the class via Schoolwork. Available in X-Protocol Version 5 and later.
- `class_number` (string): The class number. Maximum string length is 256 UTF-8 characters. Available in X-Protocol Version 4 and later.
- `course` (BaseRosterCourse): The base course for this course.
- `instructor_unique_identifiers` ([string]): Unique identification for instructors. Each string in the array has a maximum length of 256 UTF-8 characters. Value can be null.
- `location` (BaseRosterLocation): The base location for this course.
- `name` (string): The class name as displayed in Apple School Manager. Maximum length is 1024 UTF-8 characters.
- `op_date` (string): The most recent update timestamp for this class. Available in X-Protocol Version 3 and later.
- `room` (string): The room where class is held. Maximum length is 512 UTF-8 characters.
- `source` (string): The data source where class was created. Maximum length is 64 UTF-8 characters.
- `source_system_identifier` (string): The identifier configured by the organization for its classes. Maximum length is 256 UTF-8 characters. See Note.
- `status` (string): The status of the class. Possible values: `Active and Inactive`. Available in X-Protocol Version 3 and later.
- `student_unique_identifiers` ([string]): The unique identifiers for students. Each string in the array has a maximum length of 256 UTF-8 characters. Value can be null.
- `unique_identifier` (string): The global unique identifier for the class. Maximum length is 256 UTF-8 characters.

## See Also

- [Get the List of Classes](fetch-class-roster.md)
  Obtain a list of classes the server manages.
- [Sync the List of Classes](fetch-class-roster-sync.md)
  Get updates about the list of classes the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/rosterclass)*