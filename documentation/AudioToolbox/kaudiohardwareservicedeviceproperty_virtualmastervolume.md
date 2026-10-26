# kAudioHardwareServiceDeviceProperty_VirtualMasterVolume

**Framework**: Audio Toolbox  
**Kind**: case  
**Role**: Enumeration Case

A `Float32` value that represents the value of the volume control.

**Availability**:
- macOS 10.5+ - Deprecated in 10.5

## Declaration

```c
kAudioHardwareServiceDeviceProperty_VirtualMasterVolume
```

#### Discussion

The range for this property’s value is `0.0` (silence) through `1.0` (full level). The effect of this property depends on the hardware device associated with the HAL audio object. If the device has a primary volume control, this property controls it. If the device has individual channel volume controls, this property applies to those identified by the device’s preferred multichannel layout, or the preferred stereo pair if the device is stereo only. This control maintains relative balance between the channels it affects.

## See Also

### Constants
- [var kAudioHardwareServiceProperty_ServiceRestarted: AudioObjectPropertySelector](./kaudiohardwareserviceproperty_servicerestarted.md)
  Used, with a HAL audio object property listener callback, as a flag that indicates a hardware service restart. The property’s `Float32` value has no meaning. When the hardware service restarts, any associated application state, such as cached data or property listener callbacks, must be re-established.
- [kAudioHardwareServiceDeviceProperty_VirtualMasterBalance](./kaudiohardwareservicedeviceproperty_virtualmasterbalance.md)
  A `Float32` value that represents the value of a hardware device’s stereo balance control.
- [var kAudioHardwareServiceDeviceProperty_VirtualMainBalance: AudioObjectPropertySelector](./kaudiohardwareservicedeviceproperty_virtualmainbalance.md)
- [var kAudioHardwareServiceDeviceProperty_VirtualMainVolume: AudioObjectPropertySelector](./kaudiohardwareservicedeviceproperty_virtualmainvolume.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiohardwareservicedeviceproperty_virtualmastervolume)*