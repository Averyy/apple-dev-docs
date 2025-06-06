# kAudioHardwareServiceProperty_ServiceRestarted

**Framework**: Audio Toolbox  
**Kind**: var

Used, with a HAL audio object property listener callback, as a flag that indicates a hardware service restart. The property’s `Float32` value has no meaning. When the hardware service restarts, any associated application state, such as cached data or property listener callbacks, must be re-established.

**Availability**:
- macOS ?+

## Declaration

```swift
var kAudioHardwareServiceProperty_ServiceRestarted: AudioObjectPropertySelector { get }
```

## See Also

- [var kAudioHardwareServiceDeviceProperty_VirtualMainBalance: AudioObjectPropertySelector](kaudiohardwareservicedeviceproperty_virtualmainbalance.md)
- [var kAudioHardwareServiceDeviceProperty_VirtualMainVolume: AudioObjectPropertySelector](kaudiohardwareservicedeviceproperty_virtualmainvolume.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiohardwareserviceproperty_servicerestarted)*