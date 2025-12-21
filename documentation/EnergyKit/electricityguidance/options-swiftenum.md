# ElectricityGuidance.Options

**Framework**: EnergyKit  
**Kind**: enum

An enumeration that describes additional factors that influence the weight of a value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
enum Options
```

#### Overview

A person’s utility rate plan is an example of an additional factor that influences the weight of a value.

## Topics

### Getting the options
- [ElectricityGuidance.Options.locationHasRatePlan](electricityguidance/options-swift.enum/locationhasrateplan.md)
  Indicates whether the energy venue where the guidance was generated has rate plan information available.
- [ElectricityGuidance.Options.guidanceIncorporatesRatePlan](electricityguidance/options-swift.enum/guidanceincorporatesrateplan.md)
  Indicates whether the electricity guidance incorporated rate plan information.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ElectricityGuidance.Value](electricityguidance/value.md)
  A normalized weighting value associated with a period of time, describing when to shift or reduce electricity use.
- [let values: [ElectricityGuidance.Value]](electricityguidance/values.md)
  A series of weighted values for intervals of time, describing when to shift or reduce electricity use.
- [let options: Set<ElectricityGuidance.Options>](electricityguidance/options-swift.property.md)
  The additional factors that influence the weight of a value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/options-swift.enum)*