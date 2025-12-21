# ElectricityGuidance.SuggestedAction

**Framework**: EnergyKit  
**Kind**: enum

A description of how the electrical load uses the guidance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
enum SuggestedAction
```

#### Overview

An example of suggested actions for the load could be shift-able load or reduce-able load.

## Topics

### Suggesting electrical load usage
- [ElectricityGuidance.SuggestedAction.reduce](electricityguidance/suggestedaction-swift.enum/reduce.md)
  An indication of when to reduce electricity usage for devices that can reduce electricity consumption.
- [ElectricityGuidance.SuggestedAction.shift](electricityguidance/suggestedaction-swift.enum/shift.md)
  An indication of when to shift energy usage for devices that can’t reduce electricity consumption.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ElectricityGuidance.Query](electricityguidance/query.md)
  A structure that encapsulates a electricity guidance query request.
- [let suggestedAction: ElectricityGuidance.SuggestedAction](electricityguidance/suggestedaction-swift.property.md)
  A property that describes how the electrical load uses the guidance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/suggestedaction-swift.enum)*