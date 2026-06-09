# haptics

**Framework**: Game Controller  
**Kind**: property

Gets the haptics for the device, if supported.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
var haptics: GCDeviceHaptics? { get }
```

#### Discussion

Use this property to create CHHapticEngine instances according to your needs.

> **Note**: Haptics are a drain on the devices’s battery, and can be distracting when used excessively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcspatialaccessory/haptics)*