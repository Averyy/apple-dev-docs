# venue(matchingHomeUniqueIdentifier:)

**Framework**: EnergyKit  
**Kind**: method

Returns an energy venue for the given HomeKit identifier.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
static func venue(matchingHomeUniqueIdentifier: UUID) async -> EnergyVenue?
```

#### Discussion

Throws [`EnergyKitError.venueUnavailable`](energykiterror/venueunavailable.md) if a matching venue wasn’t found.

## See Also

- [static func venue(for: UUID) async -> EnergyVenue?](energyvenue/venue(for:).md)
  Returns an electricity venue for the given venue identifier, if found.
- [static func venues(near: CLLocation) async -> [EnergyVenue]](energyvenue/venues(near:).md)
  Returns a list of electricity venues near the given coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue/venue(matchinghomeuniqueidentifier:))*