# pressureConfiguration

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Configures the behavior and progression of the Force Touch trackpad when responding to recognized pressure gestures.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var pressureConfiguration: NSPressureConfiguration { get set }
```

```objc
@property (strong) NSPressureConfiguration * pressureConfiguration;
```

## Discussion

This property contains a value of type [`NSPressureConfiguration`](../nspressureconfiguration.md), which configures the behavior and progression of the Force Touch trackpad when responding to recognized pressure gestures.

Ideally, you should avoid changing the pressure configuration during recognition, as the gesture may complete before the configuration has time to take effect. If you do need to change the pressure configuration during recognition, call the [`set()`](../nspressureconfiguration/set%28%29.md) method of [`pressureConfiguration`](./pressureconfiguration.md).

Once the gesture ends or if recognition fails, the pressure configuration resets to the current view’s pressure configuration, if any, for the remaining duration of the gesture.

## See Also

### Related Documentation
- [class NSPressureConfiguration](../nspressureconfiguration.md)
  An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.
- [NSEvent.PressureBehavior](../nsevent/pressurebehavior-swift.enum.md)
  These constants describe the behavior and progression of a pressure gesture.
- [func set()](../nspressureconfiguration/set%28%29.md)
  Changes the pressure configuration of the trackpad to the initialized pressure configuration.
- [init(pressureBehavior: NSEvent.PressureBehavior)](../nspressureconfiguration/init%28pressurebehavior%29.md)
  Initializes a pressure configuration object with a specified pressure behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/pressureconfiguration)*