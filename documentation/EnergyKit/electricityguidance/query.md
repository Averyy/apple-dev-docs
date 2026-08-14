# ElectricityGuidance.Query

**Framework**: EnergyKit  
**Kind**: struct

A structure that encapsulates a electricity guidance query request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct Query
```

#### Overview

Create a [`ElectricityGuidance.Query`](electricityguidance/query.md) for a [`ElectricityGuidance.Service`](electricityguidance/service.md) request.

## Topics

### Creating a query
- [init(suggestedAction: ElectricityGuidance.SuggestedAction)](electricityguidance/query/init(suggestedaction:).md)
  Creates a query to obtain electricity guidance based on forecasted energy usage.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let suggestedAction: ElectricityGuidance.SuggestedAction](electricityguidance/suggestedaction-swift.property.md)
  A property that describes how the electrical load uses the guidance.
- [ElectricityGuidance.SuggestedAction](electricityguidance/suggestedaction-swift.enum.md)
  A description of how the electrical load uses the guidance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/query)*