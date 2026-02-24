# BaseRosterLocation

**Framework**: Device Management  
**Kind**: dictionary

A base location’s properties and their values.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object BaseRosterLocation
```

## Properties

- `name` (string): The location name. The maximum length is 1024 UTF-8 characters.
- `unique_identifier` (string): The global unique identifier for the location. The maximum length is 256 UTF-8 characters.

## See Also

- [object RosterLocation](rosterlocation.md)
  A location’s properties and their values.
- [Get the List of Locations](fetch-location-roster.md)
  Obtain a list of the locations the server manages.
- [Sync the Locations](fetch-location-roster-sync.md)
  Get updates about the list of locations the server manages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/baserosterlocation)*