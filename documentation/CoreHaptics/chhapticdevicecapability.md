# CHHapticDeviceCapability

**Framework**: Core Haptics  
**Kind**: protocol  
**Role**: Protocol

A protocol that defines haptics and audio capabilities of a device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol CHHapticDeviceCapability
```

```objc
@protocol CHHapticDeviceCapability
```

## Topics

### Determining Support for Haptics
- [var supportsAudio: Bool](./chhapticdevicecapability/supportsaudio.md)
  A Boolean value that indicates whether the device supports audio event playback.
- [var supportsHaptics: Bool](./chhapticdevicecapability/supportshaptics.md)
  A Boolean value that indicates whether the device supports haptic event playback.
### Determining Supported Parameters
- [func attributes(forDynamicParameter: CHHapticDynamicParameter.ID) throws -> any CHHapticParameterAttributes](./chhapticdevicecapability/attributes%28fordynamicparameter%29.md)
  Requests the haptic device’s attributes for a dynamic parameter.
- [func attributes(forEventParameter: CHHapticEvent.ParameterID, eventType: CHHapticEvent.EventType) throws -> any CHHapticParameterAttributes](./chhapticdevicecapability/attributes%28foreventparameter,eventtype%29.md)
  Returns the haptic device’s attributes for an event parameter.

## See Also

### Querying System Capabilities
- [class func capabilitiesForHardware() -> any CHHapticDeviceCapability](./chhapticengine/capabilitiesforhardware%28%29.md)
  Returns a device capability object that describes the device’s haptic support and limitations.
- [protocol CHHapticParameterAttributes](./chhapticparameterattributes.md)
  A protocol for providing default, mininum, and maximum values of a parameter.
- [func attributes(forDynamicParameter: CHHapticDynamicParameter.ID) throws -> any CHHapticParameterAttributes](./chhapticdevicecapability/attributes%28fordynamicparameter%29.md)
  Requests the haptic device’s attributes for a dynamic parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdevicecapability)*