# kAudioHardwareServiceDeviceProperty_VirtualMainVolume

**Framework**: Audio Toolbox  
**Kind**: var

**Availability**:
- macOS ?+

## Declaration

```swift
var kAudioHardwareServiceDeviceProperty_VirtualMainVolume: AudioObjectPropertySelector { get }
```

## See Also

- [var kAudioHardwareServiceProperty_ServiceRestarted: AudioObjectPropertySelector](kaudiohardwareserviceproperty_servicerestarted.md)
  Used, with a HAL audio object property listener callback, as a flag that indicates a hardware service restart. The property’s `Float32` value has no meaning. When the hardware service restarts, any associated application state, such as cached data or property listener callbacks, must be re-established.
- [var kAudioHardwareServiceDeviceProperty_VirtualMainBalance: AudioObjectPropertySelector](kaudiohardwareservicedeviceproperty_virtualmainbalance.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiohardwareservicedeviceproperty_virtualmainvolume)*