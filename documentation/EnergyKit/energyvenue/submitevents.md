# submitEvents(_:)

**Framework**: EnergyKit  
**Kind**: method

Submits electrical load events to be used by EnergyKit to generate energy insights.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
func submitEvents<Event>(_ events: [Event]) async throws where Event : ElectricalLoadEventProtocol
```

#### Discussion

The submission may contain events for multiple devices. The system throws [`EnergyKitError.invalidLoadEvent`](energykiterror/invalidloadevent.md) if a load event is submitted for an incorrect [`EnergyVenue`](energyvenue.md) or if it’s submitted by an iPhone, iPad, or Mac that didn’t fetch the corresponding [`ElectricityGuidance`](electricityguidance.md).

## Parameters

- `events`: An array of   conforming  load events to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/energyvenue/submitevents(_:))*