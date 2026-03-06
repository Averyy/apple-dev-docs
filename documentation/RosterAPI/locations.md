# Locations

**Framework**: Roster API  
**Kind**: dictionary

A list of locations, with a token for pagination.

**Availability**:
- Roster API 1.0.0+

## Declaration

```swift
object Locations
```

## Properties

- `locations` ([Location]): A list of [`Location`](location.md) objects.
- `moreToFollow` (boolean): A flag that indicates whether there are more locations. If `true`, use the `nextPageToken` to request another list from the remaining locations.
- `nextPageToken` (string): A token to request additional locations, if any. Use this as the `nextPageToken` parameter for the [`List locations`](returns-a-list-of-locations-for-an-apple-school-manager-organization.md) request.

## See Also

- [Read a location](returns-a-specific-location-in-an-apple-school-manager-organization.md)
  Returns a specific location in an Apple School Manager organization.
- [object Location](location.md)
  A location in an Apple School Manager organization.
- [List locations](returns-a-list-of-locations-for-an-apple-school-manager-organization.md)
  Returns a list of locations in an Apple School Manager organization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/rosterapi/locations)*