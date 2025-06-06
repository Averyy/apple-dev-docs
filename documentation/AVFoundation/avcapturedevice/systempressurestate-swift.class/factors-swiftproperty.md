# factors

**Framework**: AVFoundation  
**Kind**: property

The set of underlying causes for the system pressure level.

**Availability**:
- iOS 11.1+
- iPadOS 11.1+
- Mac Catalyst 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var factors: AVCaptureDevice.SystemPressureState.Factors { get }
```

#### Discussion

Increased system pressure may be due to one or more contributing causes; this set provides additional details for the overall performance characterization reported by the [`level`](avcapturedevice/systempressurestate-swift.class/level-swift.property.md) property.

When the system pressure level is high, you can use this information to choose how to mitigate the issue. For example, you can reduce high system pressure due to [`depthModuleTemperature`](avcapturedevice/systempressurestate-swift.class/factors-swift.struct/depthmoduletemperature.md) (on a [`builtInTrueDepthCamera`](avcapturedevice/devicetype-swift.struct/builtintruedepthcamera.md) device) by limiting the depth capture frame rate.

## See Also

- [AVCaptureDevice.SystemPressureState.Factors](avcapturedevice/systempressurestate-swift.class/factors-swift.struct.md)
  A structure that defines the factors affecting capture system performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.property)*