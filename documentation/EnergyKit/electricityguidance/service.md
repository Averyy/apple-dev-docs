# ElectricityGuidance.Service

**Framework**: EnergyKit  
**Kind**: class  
**Role**: Class

An interface for obtaining electricity guidance data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst

## Declaration

```swift
final class Service
```

## Topics

### Obtaining guidance data
- [func guidance(using: ElectricityGuidance.Query, at: UUID) -> some AsyncSequence<ElectricityGuidance, any Error>
](./service/guidance%28using,at%29.md)
  Returns an async sequence of electricity guidance forecasts for the requested venue with cost information incorporated, if available.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the electricity guidance data
- [static let sharedService: ElectricityGuidance.Service](./sharedservice.md)
  A single, shared guidance service object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electricityguidance/service)*