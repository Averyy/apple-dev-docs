# ElectricityGuidance.Service

**Framework**: EnergyKit  
**Kind**: class

An interface for obtaining electricity guidance data.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)

## Declaration

```swift
final class Service
```

## Topics

### Obtaining guidance data
- [func guidance(using: ElectricityGuidance.Query, at: UUID) -> some AsyncSequence<ElectricityGuidance, any Error>
](electricityguidance/service/guidance(using:at:).md)
  Returns an async sequence of electricity guidance forecasts for the requested venue with cost information incorporated, if available.
- [func guidance(using: ElectricityGuidance.Query, for: CLLocation) -> some AsyncSequence<ElectricityGuidance, any Error>
](electricityguidance/service/guidance(using:for:).md)
  Returns an async sequence of electricity guidance forecasts without cost information incorporated.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let sharedService: ElectricityGuidance.Service](electricityguidance/sharedservice.md)
  A single, shared guidance service object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/service)*