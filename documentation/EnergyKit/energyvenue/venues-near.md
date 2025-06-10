# venues(near:)

**Framework**: EnergyKit  
**Kind**: method

Returns a list of electricity venues near the given coordinates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
static func venues(near coordinates: CLLocation) async -> [EnergyVenue]
```

## Parameters

- `coordinates`: The   for the point of interest.

## See Also

- [static func venue(for: UUID) async -> EnergyVenue?](energyvenue/venue(for:).md)
  Returns an electricity venue for the given venue identifier, if found.
- [static func venue(matchingHomeUniqueIdentifier: UUID) async -> EnergyVenue?](energyvenue/venue(matchinghomeuniqueidentifier:).md)
  Returns an energy venue for the given HomeKit identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue/venues(near:))*