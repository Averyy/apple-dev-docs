# ElectricityGuidance.Query

**Framework**: EnergyKit  
**Kind**: struct  
**Role**: Structure

A structure that encapsulates a electricity guidance query request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
struct Query
```

#### Overview

Create a [`ElectricityGuidance.Query`](./query.md) for a [`ElectricityGuidance.Service`](./service.md) request.

## Topics

### Creating a query
- [init(suggestedAction: ElectricityGuidance.SuggestedAction)](./query/init%28suggestedaction%29.md)
  Creates a query to obtain electricity guidance based on forecasted energy usage.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the guidance suggestion
- [let suggestedAction: ElectricityGuidance.SuggestedAction](./suggestedaction-swift.property.md)
  A property that describes how the electrical load uses the guidance.
- [ElectricityGuidance.SuggestedAction](./suggestedaction-swift.enum.md)
  A description of how the electrical load uses the guidance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/query)*