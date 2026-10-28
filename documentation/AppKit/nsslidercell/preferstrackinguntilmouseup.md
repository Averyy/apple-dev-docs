# prefersTrackingUntilMouseUp

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns a Boolean value indicating whether the `NSSliderCell` continues to track the pointer until the next mouse up.

**Availability**:
- macOS

## Declaration

```swift
class var prefersTrackingUntilMouseUp: Bool { get }
```

```objc
@property (class, readonly) BOOL prefersTrackingUntilMouseUp;
```

## Return Value

[`true`](../../Swift/true.md) if the `NSSliderCell` continues to track the pointer even after it leaves the cell’s tracking rectangle; otherwise, [`false`](../../Swift/false.md). By default, this method returns [`true`](../../Swift/true.md).

## Discussion

If this method returns [`true`](../../Swift/true.md), users retain control of the knob until they release the mouse button, even if they drag the pointer to the other side of the screen.

You should not call this method explicitly. Override it if you create a subclass of `NSSliderCell` that should track the mouse differently.

## See Also

### Managing Cell Behavior
- [var altIncrementValue: Double](./altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the knob.
- [var trackRect: NSRect](./trackrect.md)
  The rectangle within which the cell tracks the pointer while the mouse button is down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/preferstrackinguntilmouseup)*