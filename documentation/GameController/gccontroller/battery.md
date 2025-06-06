# battery

**Framework**: Game Controller  
**Kind**: property

The controller’s battery information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var battery: GCDeviceBattery? { get }
```

#### Discussion

Use this property to display the battery life or to warn the user when the controller’s battery level is low. If the controller doesn’t provide battery information, this property is `nil`.

## See Also

- [var haptics: GCDeviceHaptics?](gccontroller/haptics.md)
  The controller’s haptics information.
- [var light: GCDeviceLight?](gccontroller/light.md)
  The controller’s light settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/battery)*