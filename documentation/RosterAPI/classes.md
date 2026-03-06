# Classes

**Framework**: Roster API  
**Kind**: dictionary

A list of classes, with a token for pagination.

**Availability**:
- Roster API 1.0.0+

## Declaration

```swift
object Classes
```

## Properties

- `classes` ([Class]): A list of [`Class`](class.md) objects.
- `moreToFollow` (boolean): A flag that indicates whether there are more classes. If `true`, use the `nextPageToken` to request another list from the remaining classes.
- `nextPageToken` (string): A token to request additional classes, if any. Use this as the `nextPageToken` parameter for the [`List classes`](returns-a-list-of-classes-for-an-apple-school-manager-organization.md) request.

## See Also

- [Read a class](returns-a-specific-class-in-an-apple-school-manager-organization..md)
  Read a class from an Apple School Manager organization.
- [object Class](class.md)
  A class in an Apple School Manager organization.
- [List classes](returns-a-list-of-classes-for-an-apple-school-manager-organization.md)
  List classes in an Apple School Manager organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/classes)*