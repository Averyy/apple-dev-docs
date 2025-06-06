# velocity(in:)

**Framework**: AppKit  
**Kind**: method

The velocity of the pan, measured in points per second.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func velocity(in view: NSView?) -> NSPoint
```

#### Return Value

The horizontal and vertical velocity of the pan gesture. These values are relative to the specified view.

## Parameters

- `view`: The view that provides the coordinate system for computing the velocity value. This parameter must not be  .

## See Also

- [func translation(in: NSView?) -> NSPoint](nspangesturerecognizer/translation(in:).md)
  The distance traveled by the mouse during the gesture.
- [func setTranslation(NSPoint, in: NSView?)](nspangesturerecognizer/settranslation(_:in:).md)
  Changes the current translation value of the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/velocity(in:))*