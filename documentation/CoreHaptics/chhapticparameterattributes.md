# CHHapticParameterAttributes

**Framework**: Core Haptics  
**Kind**: protocol

A protocol for providing default, mininum, and maximum values of a parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
protocol CHHapticParameterAttributes : NSObjectProtocol
```

## Topics

### Parameter Attributes
- [var defaultValue: Float](chhapticparameterattributes/defaultvalue.md)
  The default value of the parameter value.
- [var minValue: Float](chhapticparameterattributes/minvalue.md)
  The minimum value the parameter can take.
- [var maxValue: Float](chhapticparameterattributes/maxvalue.md)
  The maximum value the parameter can take.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class func capabilitiesForHardware() -> any CHHapticDeviceCapability](chhapticengine/capabilitiesforhardware.md)
  Returns a device capability object that describes the device’s haptic support and limitations.
- [protocol CHHapticDeviceCapability](chhapticdevicecapability.md)
  A protocol that defines haptics and audio capabilities of a device.
- [func attributes(forDynamicParameter: CHHapticDynamicParameter.ID) throws -> any CHHapticParameterAttributes](chhapticdevicecapability/attributes(fordynamicparameter:).md)
  Requests the haptic device’s attributes for a dynamic parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticparameterattributes)*