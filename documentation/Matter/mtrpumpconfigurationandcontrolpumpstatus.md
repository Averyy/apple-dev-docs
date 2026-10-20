# MTRPumpConfigurationAndControlPumpStatus

**Framework**: Matter  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 16.1+ - Deprecated in 16.5
- iPadOS 16.1+ - Deprecated in 16.5
- Mac Catalyst 16.1+ - Deprecated in 16.5
- macOS 13.0+ - Deprecated in 13.4
- tvOS 16.1+ - Deprecated in 16.5
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.1+ - Deprecated in 9.5

> **Deprecated**: Please use MTRPumpConfigurationAndControlPumpStatusBitmap

## Declaration

```swift
struct MTRPumpConfigurationAndControlPumpStatus
```

```c
enum MTRPumpConfigurationAndControlPumpStatus : uint16_t;
```

## Topics

### Initializers
- [init(rawValue: UInt16)](./mtrpumpconfigurationandcontrolpumpstatus/init%28rawvalue%29.md)
### Type Properties
- [static var deviceFault: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/devicefault.md)
- [static var localOverride: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/localoverride.md)
- [static var remoteFlow: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/remoteflow.md)
- [static var remotePressure: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/remotepressure.md)
- [static var remoteTemperature: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/remotetemperature.md)
- [static var running: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/running.md)
- [static var speedHigh: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/speedhigh.md)
- [static var speedLow: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/speedlow.md)
- [static var supplyfault: MTRPumpConfigurationAndControlPumpStatus](./mtrpumpconfigurationandcontrolpumpstatus/supplyfault.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/matter/mtrpumpconfigurationandcontrolpumpstatus)*