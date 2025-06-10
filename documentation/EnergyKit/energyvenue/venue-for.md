# venue(for:)

**Framework**: EnergyKit  
**Kind**: method

Returns an electricity venue for the given venue identifier, if found.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
static func venue(for id: UUID) async -> EnergyVenue?
```

#### Discussion

Throws [`EnergyKitError.venueUnavailable`](energykiterror/venueunavailable.md) if the system didn’t find a matching venue.

## Parameters

- `id`: The venue identifier.

## See Also

- [static func venue(matchingHomeUniqueIdentifier: UUID) async -> EnergyVenue?](energyvenue/venue(matchinghomeuniqueidentifier:).md)
  Returns an energy venue for the given HomeKit identifier.
- [static func venues(near: CLLocation) async -> [EnergyVenue]](energyvenue/venues(near:).md)
  Returns a list of electricity venues near the given coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue/venue(for:))*