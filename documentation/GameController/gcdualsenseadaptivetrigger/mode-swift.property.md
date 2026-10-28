# mode

**Framework**: Game Controller  
**Kind**: property  
**Role**: Instance Property

The current configuration of the adaptive trigger.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+
- visionOS 1.0+

## Declaration

```swift
var mode: GCDualSenseAdaptiveTrigger.Mode { get }
```

```objc
@property (nonatomic, readonly) GCDualSenseAdaptiveTriggerMode mode;
```

## Discussion

There may be a delay updating this property value after you set the mode using one of the set mode methods because setting the mode requires a response from the controller.

## See Also

### Getting the mode
- [GCDualSenseAdaptiveTrigger.Mode](./mode-swift.enum.md)
  The possible modes of an adaptive trigger.
- [func setModeOff()](./setmodeoff%28%29.md)
  Sets the mode to off and stops any trigger effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/mode-swift.property)*