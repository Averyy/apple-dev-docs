# prefersTrackingUntilMouseUp

**Framework**: AppKit  
**Kind**: property

Returns a Boolean value indicating whether the `NSSliderCell` continues to track the pointer until the next mouse up.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var prefersTrackingUntilMouseUp: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the `NSSliderCell` continues to track the pointer even after it leaves the cell’s tracking rectangle; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). By default, this method returns [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

If this method returns [`true`](https://developer.apple.com/documentation/swift/true), users retain control of the knob until they release the mouse button, even if they drag the pointer to the other side of the screen.

You should not call this method explicitly. Override it if you create a subclass of `NSSliderCell` that should track the mouse differently.

## See Also

- [var altIncrementValue: Double](nsslidercell/altincrementvalue.md)
  The amount by which the slider changes its value when the user Option-drags the knob.
- [var trackRect: NSRect](nsslidercell/trackrect.md)
  The rectangle within which the cell tracks the pointer while the mouse button is down.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsslidercell/preferstrackinguntilmouseup)*