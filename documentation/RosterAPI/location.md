# Location

**Framework**: Roster API  
**Kind**: dictionary

A location in an Apple School Manager organization.

**Availability**:
- Roster API 1.0.0+

## Declaration

```swift
object Location
```

## Properties

- `dateCreated` (string): The date the location object was created in Apple School Manager. The date string is in ISO 8601 format.
- `dateLastModified` (string): The date the location object was modified in Apple School Manager. The date string is in ISO 8601 format.
- `domain` (string): The location’s domain.
- `id` (string): The location’s identifier.
- `name` (string): The location’s name.
- `timeZone` (string): The time zone used at the location.

## See Also

- [Read a location](returns-a-specific-location-in-an-apple-school-manager-organization.md)
  Returns a specific location in an Apple School Manager organization.
- [List locations](returns-a-list-of-locations-for-an-apple-school-manager-organization.md)
  Returns a list of locations in an Apple School Manager organization.
- [object Locations](locations.md)
  A list of locations, with a token for pagination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/location)*