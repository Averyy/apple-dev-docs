# ElectricityGuidance.SuggestedAction

**Framework**: EnergyKit  
**Kind**: enum  
**Role**: Enumeration

A description of how the electrical load uses the guidance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
enum SuggestedAction
```

## Mentions

- [Providing charging history for electric vehicles](../providing-informative-charging-history-for-electric-vehicles.md)

## Overview

An example of suggested actions for the load could be shift-able load or reduce-able load.

## Topics

### Suggesting electrical load usage
- [ElectricityGuidance.SuggestedAction.reduce](./suggestedaction-swift.enum/reduce.md)
  An indication of when to reduce electricity usage for devices that can reduce electricity consumption.
- [ElectricityGuidance.SuggestedAction.shift](./suggestedaction-swift.enum/shift.md)
  An indication of when to shift energy usage for devices that can’t reduce electricity consumption.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the guidance suggestion
- [ElectricityGuidance.Query](./query.md)
  A structure that encapsulates a electricity guidance query request.
- [let suggestedAction: ElectricityGuidance.SuggestedAction](./suggestedaction-swift.property.md)
  A property that describes how the electrical load uses the guidance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/suggestedaction-swift.enum)*