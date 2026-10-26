# kAudioHardwareServiceDeviceProperty_VirtualMasterBalance

**Framework**: Audio Toolbox  
**Kind**: case  
**Role**: Enumeration Case

A `Float32` value that represents the value of a hardware device’s stereo balance control.

**Availability**:
- macOS 10.5+ - Deprecated in 10.5

## Declaration

```c
kAudioHardwareServiceDeviceProperty_VirtualMasterBalance
```

#### Discussion

The range for this property’s value is `0.0` (full left) through `1.0` (full right). A value of `0.5` means that both channels of the default stereo pair have equal power. This control is available only for hardware devices that have individual channel volume controls.

## See Also

### Constants
- [var kAudioHardwareServiceProperty_ServiceRestarted: AudioObjectPropertySelector](./kaudiohardwareserviceproperty_servicerestarted.md)
  Used, with a HAL audio object property listener callback, as a flag that indicates a hardware service restart. The property’s `Float32` value has no meaning. When the hardware service restarts, any associated application state, such as cached data or property listener callbacks, must be re-established.
- [kAudioHardwareServiceDeviceProperty_VirtualMasterVolume](./kaudiohardwareservicedeviceproperty_virtualmastervolume.md)
  A `Float32` value that represents the value of the volume control.
- [var kAudioHardwareServiceDeviceProperty_VirtualMainBalance: AudioObjectPropertySelector](./kaudiohardwareservicedeviceproperty_virtualmainbalance.md)
- [var kAudioHardwareServiceDeviceProperty_VirtualMainVolume: AudioObjectPropertySelector](./kaudiohardwareservicedeviceproperty_virtualmainvolume.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiohardwareservicedeviceproperty_virtualmasterbalance)*