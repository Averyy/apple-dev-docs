# haptics

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

Gets the haptics profile for the stylus, if supported.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var haptics: GCDeviceHaptics? { get }
```

```objc
@property (strong, readonly, nullable) GCDeviceHaptics * haptics;
```

#### Discussion

The haptics profile is represented as a `GCDeviceHaptics` instance, from which you can create `CHHapticEngine` instances targeting the haptic actuator(s) in the accessory.

Not all stylus accessories support haptic feedback.  If the accessory does not support haptic feedback, this property is `nil`.

> **Note**: Haptics are a drain on the accessory’s battery, and can be distracting when used excessively. Use haptic feedback judiciously and in response to meaningful user interactions.

## See Also

### Getting input values and haptics
- [var input: (any GCDevicePhysicalInput)?](./input.md)
  Gets the input profile for the stylus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcstylus/haptics)*