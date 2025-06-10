# ElectricityGuidance.Query

**Framework**: EnergyKit  
**Kind**: struct

A structure that encapsulates a electricity guidance query request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

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
### Decoding
- [init(from: any Decoder) throws](electricityguidance/query/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](electricityguidance/query/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let suggestedAction: ElectricityGuidance.SuggestedAction](electricityguidance/suggestedaction-swift.property.md)
  A property that describes how the electrical load uses the guidance.
- [ElectricityGuidance.SuggestedAction](electricityguidance/suggestedaction-swift.enum.md)
  A description of how the electrical load uses the guidance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/query)*