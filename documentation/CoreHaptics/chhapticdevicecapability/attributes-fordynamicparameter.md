# attributes(forDynamicParameter:)

**Framework**: Core Haptics  
**Kind**: method  
**Required**: Yes

Requests the haptic device’s attributes for a dynamic parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func attributes(forDynamicParameter inParameter: CHHapticDynamicParameter.ID) throws -> any CHHapticParameterAttributes
```

#### Return Value

The haptic device’s attributes for the given dynamic parameter ID.

## Parameters

- `inParameter`: The dynamic parameter ID whose attributes you seek.

## See Also

- [class func capabilitiesForHardware() -> any CHHapticDeviceCapability](chhapticengine/capabilitiesforhardware.md)
  Returns a device capability object that describes the device’s haptic support and limitations.
- [protocol CHHapticDeviceCapability](chhapticdevicecapability.md)
  A protocol that defines haptics and audio capabilities of a device.
- [protocol CHHapticParameterAttributes](chhapticparameterattributes.md)
  A protocol for providing default, mininum, and maximum values of a parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticdevicecapability/attributes(fordynamicparameter:))*