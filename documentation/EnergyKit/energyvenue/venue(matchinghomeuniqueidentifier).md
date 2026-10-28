# venue(matchingHomeUniqueIdentifier:)

**Framework**: EnergyKit  
**Kind**: method  
**Role**: Type Method

Returns an energy venue for the given HomeKit identifier.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst

## Declaration

```swift
static func venue(matchingHomeUniqueIdentifier: UUID) async throws -> EnergyVenue
```

## Discussion

This method throws [`EnergyKitError.venueUnavailable`](../energykiterror/venueunavailable.md) if the framework can’t provide the requested venue.

## Parameters

- `matchingHomeUniqueIdentifier`: A HomeKit identifier for the requested venue.

## See Also

### Returning electricity sites
- [static func venue(for: UUID) async throws -> EnergyVenue](./venue%28for%29.md)
  Returns an electricity venue for the given venue identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue/venue(matchinghomeuniqueidentifier:))*