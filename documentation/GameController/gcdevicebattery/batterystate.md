# batteryState

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The state of a device’s battery.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var batteryState: GCDeviceBattery.State { get }
```

```objc
@property (nonatomic, readonly) GCDeviceBatteryState batteryState;
```

## See Also

### Getting the battery level and state
- [var batteryLevel: Float](./batterylevel.md)
  The charge level of a device’s battery.
- [GCDeviceBattery.State](./state.md)
  A state that indicates whether a device’s battery has power and is charging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdevicebattery/batterystate)*