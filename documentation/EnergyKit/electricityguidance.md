# ElectricityGuidance

**Framework**: EnergyKit  
**Kind**: struct

A data model that provides guidance on when electricity is cleaner and less expensive.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct ElectricityGuidance
```

#### Overview

`ElectricityGuidance` provides information on grid quality and electricity cost, if cost information is available. You can use `ElectricityGuidance` to adjust the electricity consumption of your managed devices to times when electricity is cleaner, and optionally reduce the overall electricity consumption or cost of your managed devices.

## Topics

### Getting the electricity guidance data
- [ElectricityGuidance.Service](electricityguidance/service.md)
  An interface for obtaining electricity guidance data.
- [static let sharedService: ElectricityGuidance.Service](electricityguidance/sharedservice.md)
  A single, shared guidance service object.
### Getting the electrical load weight
- [ElectricityGuidance.Value](electricityguidance/value.md)
  A normalized weighting value associated with a period of time, describing when to shift or reduce electricity use.
- [let values: [ElectricityGuidance.Value]](electricityguidance/values.md)
  A series of weighted values for intervals of time, describing when to shift or reduce electricity use.
- [ElectricityGuidance.Options](electricityguidance/options-swift.enum.md)
  An enumeration that describes additional factors that influence the weight of a value.
- [let options: Set<ElectricityGuidance.Options>](electricityguidance/options-swift.property.md)
  The additional factors that influence the weight of a value.
### Identifying the guidance parameters
- [let interval: DateInterval](electricityguidance/interval.md)
  The time range to which the guidance applies.
- [let energyVenueID: UUID](electricityguidance/energyvenueid.md)
  An identifier for the physical location to which the guidance applies.
- [let guidanceToken: UUID](electricityguidance/guidancetoken.md)
  A unique token for the guidance that you use to create an electrical load event.
### Getting the guidance suggestion
- [ElectricityGuidance.Query](electricityguidance/query.md)
  A structure that encapsulates a electricity guidance query request.
- [let suggestedAction: ElectricityGuidance.SuggestedAction](electricityguidance/suggestedaction-swift.property.md)
  A property that describes how the electrical load uses the guidance.
- [ElectricityGuidance.SuggestedAction](electricityguidance/suggestedaction-swift.enum.md)
  A description of how the electrical load uses the guidance.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance)*