# isEnabled

**Framework**: Touch Controller  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A Boolean value that indicates whether the control is enabled.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var isEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isEnabled) BOOL enabled;
```

## Discussion

If disabled, it won’t respond to touches.

## See Also

### Inspecting a control
- [var highlightDuration: TimeInterval](./highlightduration.md)
  The duration of the highlight animation.
- [var label: TCControlLabel](./label.md)
  The label associated with the control.
- [class TCControlLabel](../tccontrollabel.md)
  A label you associate with a touch control and provides a semantic description.
- [var isPressed: Bool](./ispressed.md)
  Indicates whether the control is currently pressed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrol/isenabled)*