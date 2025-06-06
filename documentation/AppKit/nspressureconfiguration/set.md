# set()

**Framework**: AppKit  
**Kind**: method

Changes the pressure configuration of the trackpad to the initialized pressure configuration.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
func set()
```

#### Discussion

During a mouse drag or pressure event sequence, this method may be called to change the pressure configuration of the trackpad to the initialized pressure configuration. The trackpad’s pressure configuration is automatically reset when the user releases the mouse or ends the gesture. If called outside of a mouse drag or pressure event sequence, this method has no effect on the trackpad.

Ideally, pressure behavior should be configured by adjusting the `pressureConfiguration` property of a view prior to a mouse drag or gesture event occurring, such as before the view is displayed. Otherwise, the user may complete the mouse drag or gesture before the configuration has time to take effect.

## See Also

- [class NSView](nsview.md)
  The infrastructure for drawing, printing, and handling events in an app.
- [init(pressureBehavior: NSEvent.PressureBehavior)](nspressureconfiguration/init(pressurebehavior:).md)
  Initializes a pressure configuration object with a specified pressure behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressureconfiguration/set())*