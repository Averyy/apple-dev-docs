# ProcessInfo.ThermalState.critical

**Framework**: Foundation  
**Kind**: case

The thermal state is significantly impacting the performance of the system and the device needs to cool down.

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
case critical
```

#### Discussion

The system takes significant steps to reduce thermal state. Fans are running at maximum speed.

Reduce usage of the CPU, GPU, and I/O such as Bluetooth or network to the minimum level required for user interaction. If possible, stop using peripherals such as the camera, flash, microphone, and speaker.

## See Also

- [ProcessInfo.ThermalState.nominal](processinfo/thermalstate-swift.enum/nominal.md)
  The thermal state is within normal limits.
- [ProcessInfo.ThermalState.fair](processinfo/thermalstate-swift.enum/fair.md)
  The thermal state is slightly elevated.
- [ProcessInfo.ThermalState.serious](processinfo/thermalstate-swift.enum/serious.md)
  The thermal state is high.
- [ProcessInfo.ThermalState.nominal](processinfo/thermalstate-swift.enum/nominal.md)
  The thermal state is within normal limits.
- [ProcessInfo.ThermalState.fair](processinfo/thermalstate-swift.enum/fair.md)
  The thermal state is slightly elevated.
- [ProcessInfo.ThermalState.serious](processinfo/thermalstate-swift.enum/serious.md)
  The thermal state is high.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum/critical)*