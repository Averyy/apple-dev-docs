# ProcessInfo.ThermalState.fair

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

The thermal state is slightly elevated.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.10.3+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case fair
```

```c
NSProcessInfoThermalStateFair
```

#### Discussion

The system takes steps to reduce thermal state, like running fans and stopping background services that aren’t doing work immediately needed by the user.

Reduce or defer background work, like prefetching content over the network or updating database indexes.

## See Also

### Constants
- [ProcessInfo.ThermalState.nominal](./nominal.md)
  The thermal state is within normal limits.
- [ProcessInfo.ThermalState.serious](./serious.md)
  The thermal state is high.
- [ProcessInfo.ThermalState.critical](./critical.md)
  The thermal state is significantly impacting the performance of the system and the device needs to cool down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum/fair)*