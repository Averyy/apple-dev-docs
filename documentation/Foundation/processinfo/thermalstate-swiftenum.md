# ProcessInfo.ThermalState

**Framework**: Foundation  
**Kind**: enum

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

#### Overview

These values are used by the [`ProcessInfo`](processinfo.md) class as return values for [`thermalState`](processinfo/thermalstate-swift.property.md).

For information about testing your app under different thermal states, see [`Test under adverse device conditions`](https://developer.apple.comhttps://help.apple.com/xcode/mac/current/#/dev308429d42).

## Topics

### Constants
- [ProcessInfo.ThermalState.nominal](processinfo/thermalstate-swift.enum/nominal.md)
  The thermal state is within normal limits.
- [ProcessInfo.ThermalState.fair](processinfo/thermalstate-swift.enum/fair.md)
  The thermal state is slightly elevated.
- [ProcessInfo.ThermalState.serious](processinfo/thermalstate-swift.enum/serious.md)
  The thermal state is high.
- [ProcessInfo.ThermalState.critical](processinfo/thermalstate-swift.enum/critical.md)
  The thermal state is significantly impacting the performance of the system and the device needs to cool down.
### Initializers
- [init?(rawValue: Int)](processinfo/thermalstate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var thermalState: ProcessInfo.ThermalState](processinfo/thermalstate-swift.property.md)
  The current thermal state of the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum)*