# ProcessInfo.ThermalState

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Values used to indicate the system’s thermal state.

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
enum ThermalState
```

```c
enum NSProcessInfoThermalState : NSInteger;
```

## Overview

These values are used by the [`ProcessInfo`](../processinfo.md) class as return values for [`thermalState`](./thermalstate-swift.property.md).

For information about testing your app under different thermal states, see [Test under adverse device conditions](https://help.apple.com/xcode/mac/current/#/dev308429d42).

## Topics

### Constants
- [ProcessInfo.ThermalState.nominal](./thermalstate-swift.enum/nominal.md)
  The thermal state is within normal limits.
- [ProcessInfo.ThermalState.fair](./thermalstate-swift.enum/fair.md)
  The thermal state is slightly elevated.
- [ProcessInfo.ThermalState.serious](./thermalstate-swift.enum/serious.md)
  The thermal state is high.
- [ProcessInfo.ThermalState.critical](./thermalstate-swift.enum/critical.md)
  The thermal state is significantly impacting the performance of the system and the device needs to cool down.
### Initializers
- [init?(rawValue: Int)](./thermalstate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the thermal state
- [var thermalState: ProcessInfo.ThermalState](./thermalstate-swift.property.md)
  The current thermal state of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum)*