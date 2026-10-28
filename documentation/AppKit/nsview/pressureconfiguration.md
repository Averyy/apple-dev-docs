# pressureConfiguration

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Configures the behavior and progression of the Force Touch trackpad when responding to touch input produced by the user when the cursor is over the view.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var pressureConfiguration: NSPressureConfiguration? { get set }
```

```objc
@property (strong, nullable) NSPressureConfiguration * pressureConfiguration;
```

## Discussion

This property configures the behavior and progression of the Force Touch trackpad when responding to touch input produced by the user when the cursor is over the view.

Changing the value of this property does not affect a pressure event that’s already active. This property must be set prior to a mouse-down event, for use with future pressure gestures.

## See Also

### Related Documentation
- [class NSPressureConfiguration](../nspressureconfiguration.md)
  An encapsulation of the behavior and progression of a Force Touch trackpad as it responds to specific events.
- [NSEvent.PressureBehavior](../nsevent/pressurebehavior-swift.enum.md)
  These constants describe the behavior and progression of a pressure gesture.
- [init(pressureBehavior: NSEvent.PressureBehavior)](../nspressureconfiguration/init%28pressurebehavior%29.md)
  Initializes a pressure configuration object with a specified pressure behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/pressureconfiguration)*