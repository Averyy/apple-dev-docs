# pressureConfiguration

**Framework**: AppKit  
**Kind**: property

Configures the behavior and progression of the Force Touch trackpad when responding to recognized pressure gestures.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var pressureConfiguration: NSPressureConfiguration { get set }
```

#### Discussion

This property contains a value of type [`NSPressureConfiguration`](nspressureconfiguration.md), which configures the behavior and progression of the Force Touch trackpad when responding to recognized pressure gestures.

Ideally, you should avoid changing the pressure configuration during recognition, as the gesture may complete before the configuration has time to take effect. If you do need to change the pressure configuration during recognition, call the [`set()`](nspressureconfiguration/set().md) method of [`pressureConfiguration`](nsgesturerecognizer/pressureconfiguration.md).

Once the gesture ends or if recognition fails, the pressure configuration resets to the current view’s pressure configuration, if any, for the remaining duration of the gesture.

## See Also

- [class NSPressureConfiguration](nspressureconfiguration.md)
  An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.
- [NSEvent.PressureBehavior](nsevent/pressurebehavior-swift.enum.md)
  These constants describe the behavior and progression of a pressure gesture.
- [func set()](nspressureconfiguration/set.md)
  Changes the pressure configuration of the trackpad to the initialized pressure configuration.
- [init(pressureBehavior: NSEvent.PressureBehavior)](nspressureconfiguration/init(pressurebehavior:).md)
  Initializes a pressure configuration object with a specified pressure behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/pressureconfiguration)*