# venue(for:)

**Framework**: EnergyKit  
**Kind**: method  
**Role**: Type Method

Returns an electricity venue for the given venue identifier.

**Availability**:
- iOS 26.1+
- iPadOS 26.1+
- Mac Catalyst

## Declaration

```swift
static func venue(for id: UUID) async throws -> EnergyVenue
```

#### Discussion

This method throws [`EnergyKitError.venueUnavailable`](../energykiterror/venueunavailable.md) if the framework can’t provide the requested venue.

## Parameters

- `id`: The requested venue’s identifier.

## See Also

### Returning electricity sites
- [static func venue(matchingHomeUniqueIdentifier: UUID) async throws -> EnergyVenue](./venue%28matchinghomeuniqueidentifier%29.md)
  Returns an energy venue for the given HomeKit identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue/venue(for:))*