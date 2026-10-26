# kAudioHardwareServiceDeviceProperty_VirtualMainBalance

**Framework**: Audio Toolbox  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- macOS

## Declaration

```swift
var kAudioHardwareServiceDeviceProperty_VirtualMainBalance: AudioObjectPropertySelector { get }
```

```c
kAudioHardwareServiceDeviceProperty_VirtualMainBalance
```

## See Also

### Constants
- [var kAudioHardwareServiceProperty_ServiceRestarted: AudioObjectPropertySelector](./kaudiohardwareserviceproperty_servicerestarted.md)
  Used, with a HAL audio object property listener callback, as a flag that indicates a hardware service restart. The property’s `Float32` value has no meaning. When the hardware service restarts, any associated application state, such as cached data or property listener callbacks, must be re-established.
- [var kAudioHardwareServiceDeviceProperty_VirtualMainVolume: AudioObjectPropertySelector](./kaudiohardwareservicedeviceproperty_virtualmainvolume.md)
- [kAudioHardwareServiceDeviceProperty_VirtualMasterVolume](./kaudiohardwareservicedeviceproperty_virtualmastervolume.md)
  A `Float32` value that represents the value of the volume control.
- [kAudioHardwareServiceDeviceProperty_VirtualMasterBalance](./kaudiohardwareservicedeviceproperty_virtualmasterbalance.md)
  A `Float32` value that represents the value of a hardware device’s stereo balance control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiohardwareservicedeviceproperty_virtualmainbalance)*