# mode

**Framework**: Game Controller  
**Kind**: property

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

#### Discussion

There may be a delay updating this property value after you set the mode using one of the set mode methods because setting the mode requires a response from the controller.

## See Also

- [GCDualSenseAdaptiveTrigger.Mode](gcdualsenseadaptivetrigger/mode-swift.enum.md)
  The possible modes of an adaptive trigger.
- [func setModeOff()](gcdualsenseadaptivetrigger/setmodeoff.md)
  Sets the mode to off and stops any trigger effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcdualsenseadaptivetrigger/mode-swift.property)*