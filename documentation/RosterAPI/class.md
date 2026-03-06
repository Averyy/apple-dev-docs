# Class

**Framework**: Roster API  
**Kind**: dictionary

A class in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Declaration

```swift
object Class
```

## Properties

- `dateCreated` (string): The date the class object was created in Apple School Manager. The date string is in ISO 8601 format.
- `dateLastModified` (string): The date the class object was modified in Apple School Manager. The date string is in ISO 8601 format.
- `id` (string): A unique identifier for this class.
- `instructorIds` ([string]): A list of user identifiers for instructers. Values refer to the `id` field of the [`User`](user.md) object.
- `room` (string): The name of the room.
- `studentIds` ([string]): A list of user identifiers for students in the class.
- `name` (string): The name of the class.
- `number` (string): The number of the class.
- `displayName` (string): The Class Nickname in Apple School Manager.
- `locationId` (string): An identifier for the class’s location.

## See Also

- [Read a class](returns-a-specific-class-in-an-apple-school-manager-organization..md)
  Read a class from an Apple School Manager organization.
- [List classes](returns-a-list-of-classes-for-an-apple-school-manager-organization.md)
  List classes in an Apple School Manager organization.
- [object Classes](classes.md)
  A list of classes, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/class)*