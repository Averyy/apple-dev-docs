# capabilitiesForHardware()

**Framework**: Core Haptics  
**Kind**: method

Returns a device capability object that describes the device’s haptic support and limitations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func capabilitiesForHardware() -> any CHHapticDeviceCapability
```

## See Also

- [protocol CHHapticDeviceCapability](chhapticdevicecapability.md)
  A protocol that defines haptics and audio capabilities of a device.
- [protocol CHHapticParameterAttributes](chhapticparameterattributes.md)
  A protocol for providing default, mininum, and maximum values of a parameter.
- [func attributes(forDynamicParameter: CHHapticDynamicParameter.ID) throws -> any CHHapticParameterAttributes](chhapticdevicecapability/attributes(fordynamicparameter:).md)
  Requests the haptic device’s attributes for a dynamic parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticengine/capabilitiesforhardware())*