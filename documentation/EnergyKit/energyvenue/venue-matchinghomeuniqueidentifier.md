# venue(matchingHomeUniqueIdentifier:)

**Framework**: EnergyKit  
**Kind**: method

Returns an energy venue for the given HomeKit identifier.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst ?+
- macOS 26.1+

## Declaration

```swift
static func venue(matchingHomeUniqueIdentifier: UUID) async throws -> EnergyVenue
```

#### Discussion

This method throws [`EnergyKitError.venueUnavailable`](energykiterror/venueunavailable.md) if the framework can’t provide the requested venue.

## Parameters

- `matchingHomeUniqueIdentifier`: A HomeKit identifier for the requested venue.

## See Also

- [static func venue(for: UUID) async throws -> EnergyVenue](energyvenue/venue(for:).md)
  Returns an electricity venue for the given venue identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue/venue(matchinghomeuniqueidentifier:))*