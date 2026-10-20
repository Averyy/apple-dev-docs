# trackRect

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The rectangle within which the cell tracks the pointer while the mouse button is down.

**Availability**:
- macOS

## Declaration

```swift
var trackRect: NSRect { get }
```

```objc
@property (readonly) NSRect trackRect;
```

#### Discussion

The tracking rectangle includes the slider bar, but not the bezel.

## See Also

### Managing Cell Behavior
- [var altIncrementValue: Double](./altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the knob.
- [class var prefersTrackingUntilMouseUp: Bool](./preferstrackinguntilmouseup.md)
  Returns a Boolean value indicating whether the `NSSliderCell` continues to track the pointer until the next mouse up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/trackrect)*