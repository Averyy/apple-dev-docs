# Audio Hardware Services Properties

**Framework**: Audio Toolbox

Property identifiers that apply to HAL audio objects only when accessed via the Audio Hardware Services.

## Topics

### Constants
- [var kAudioHardwareServiceProperty_ServiceRestarted: AudioObjectPropertySelector](kaudiohardwareserviceproperty_servicerestarted.md)
  Used, with a HAL audio object property listener callback, as a flag that indicates a hardware service restart. The property’s `Float32` value has no meaning. When the hardware service restarts, any associated application state, such as cached data or property listener callbacks, must be re-established.
- [var kAudioHardwareServiceDeviceProperty_VirtualMainBalance: AudioObjectPropertySelector](kaudiohardwareservicedeviceproperty_virtualmainbalance.md)
- [var kAudioHardwareServiceDeviceProperty_VirtualMainVolume: AudioObjectPropertySelector](kaudiohardwareservicedeviceproperty_virtualmainvolume.md)

## See Also

- [func AudioServicesGetPropertyInfo(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioservicesgetpropertyinfo(_:_:_:_:_:).md)
  Gets information about a System Sound Services property.
- [func AudioServicesGetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audioservicesgetproperty(_:_:_:_:_:).md)
  Gets a specified System Sound Services property value.
- [func AudioServicesSetProperty(AudioServicesPropertyID, UInt32, UnsafeRawPointer?, UInt32, UnsafeRawPointer) -> OSStatus](audioservicessetproperty(_:_:_:_:_:).md)
  Sets the value for a specified System Sound Services property.
- [typealias AudioServicesPropertyID](audioservicespropertyid.md)
  The data type for a system sound property identifier.
- [System Sound Services Property Identifiers](1405268-system-sound-services-property-i.md)
  Property identifiers used when playing alerts with System Sound Services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1405208-audio-hardware-services-properti)*