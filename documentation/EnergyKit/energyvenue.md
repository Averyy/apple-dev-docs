# EnergyVenue

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

A physical site that uses or produces electricity at that location.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct EnergyVenue
```

## Topics

### Returning electricity sites
- [static func venue(for: UUID) async throws -> EnergyVenue](./energyvenue/venue%28for%29.md)
  Returns an electricity venue for the given venue identifier.
- [static func venue(matchingHomeUniqueIdentifier: UUID) async throws -> EnergyVenue](./energyvenue/venue%28matchinghomeuniqueidentifier%29.md)
  Returns an energy venue for the given HomeKit identifier.
### Submitting load events
- [func submitEvents<Event>([Event]) async throws](./energyvenue/submitevents%28_%29.md)
  Submits electrical load events to be used by EnergyKit to generate energy insights.
### Identifying the location
- [let id: UUID](./energyvenue/id.md)
  A unique identifier for the venue.
- [let name: String](./energyvenue/name.md)
  The name of the Home to which the venue corresponds.
### Type Methods
- [static func venues() async throws -> [EnergyVenue]](./energyvenue/venues%28%29.md)
  Returns a list of electricity venues.

## Relationships

### Conforms To
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Identifiable](../Swift/identifiable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue)*