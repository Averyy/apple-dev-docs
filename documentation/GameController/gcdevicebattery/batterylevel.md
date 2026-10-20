# batteryLevel

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The charge level of a device’s battery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var batteryLevel: Float { get }
```

```objc
@property (nonatomic, readonly) float batteryLevel;
```

#### Discussion

The battery level is a percentage ranging from `0.0` (fully discharged) to `1.0` (100% charged). The default value for this property is `0.0`.

## See Also

### Getting the battery level and state
- [var batteryState: GCDeviceBattery.State](./batterystate.md)
  The state of a device’s battery.
- [GCDeviceBattery.State](./state.md)
  A state that indicates whether a device’s battery has power and is charging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicebattery/batterylevel)*