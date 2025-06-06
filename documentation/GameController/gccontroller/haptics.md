# haptics

**Framework**: Game Controller  
**Kind**: property

The controller’s haptics information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var haptics: GCDeviceHaptics? { get }
```

#### Discussion

Use this property to create [`CHHapticEngine`](https://developer.apple.com/documentation/CoreHaptics/CHHapticEngine) instances as necessary in your app. If the controller doesn’t provide haptics information, this property is `nil`.

## See Also

- [var battery: GCDeviceBattery?](gccontroller/battery.md)
  The controller’s battery information.
- [var light: GCDeviceLight?](gccontroller/light.md)
  The controller’s light settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/haptics)*