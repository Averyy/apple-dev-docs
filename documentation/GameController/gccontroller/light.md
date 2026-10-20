# light

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The controller’s light settings.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var light: GCDeviceLight? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) GCDeviceLight * light;
```

#### Discussion

Use the light settings to signal the user or to create a more immersive experience. If the controller doesn’t provide light settings, this property is `nil`.

## See Also

### Accessing battery, haptics, and light objects
- [var battery: GCDeviceBattery?](./battery.md)
  The controller’s battery information.
- [var haptics: GCDeviceHaptics?](./haptics.md)
  The controller’s haptics information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontroller/light)*