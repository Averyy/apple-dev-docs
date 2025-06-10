# ProcessInfo.ThermalState.serious

**Framework**: Foundation  
**Kind**: case

The thermal state is high.

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
case serious
```

#### Discussion

The system takes moderate steps to reduce thermal state, which reduces performance. Fans are running at maximum speed.

Reduce usage of resources that generate heat and consume battery, for example:

- Reduce or defer I/O operations, such as networking and Bluetooth
- Reduce the requested level of accuracy for location
- Reduce CPU and GPU usage by stopping or deferring work
- Reduce the target framerate from 60 FPS to 30 FPS
- Reduce the level of detail in rendered content by using fewer particles or lower-resolution textures

For more details on how to reduce your app’s use of these resources, see [`Energy Efficiency Guide for iOS Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/EnergyGuide-iOS/index.html#//apple_ref/doc/uid/TP40015243) and [`Energy Efficiency Guide for Mac Apps`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

## See Also

- [ProcessInfo.ThermalState.nominal](processinfo/thermalstate-swift.enum/nominal.md)
  The thermal state is within normal limits.
- [ProcessInfo.ThermalState.fair](processinfo/thermalstate-swift.enum/fair.md)
  The thermal state is slightly elevated.
- [ProcessInfo.ThermalState.critical](processinfo/thermalstate-swift.enum/critical.md)
  The thermal state is significantly impacting the performance of the system and the device needs to cool down.
- [ProcessInfo.ThermalState.nominal](processinfo/thermalstate-swift.enum/nominal.md)
  The thermal state is within normal limits.
- [ProcessInfo.ThermalState.fair](processinfo/thermalstate-swift.enum/fair.md)
  The thermal state is slightly elevated.
- [ProcessInfo.ThermalState.critical](processinfo/thermalstate-swift.enum/critical.md)
  The thermal state is significantly impacting the performance of the system and the device needs to cool down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processinfo/thermalstate-swift.enum/serious)*