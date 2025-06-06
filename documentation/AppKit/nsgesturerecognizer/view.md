# view

**Framework**: AppKit  
**Kind**: property

The view to which the gesture recognizer is attached.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var view: NSView? { get }
```

#### Discussion

To attach a gesture recognizer to a view, call the [`addGestureRecognizer(_:)`](nsview/addgesturerecognizer(_:).md) method of the view. If the gesture recognizer is not attached to a view, the value in this property is `nil`.

## See Also

- [func location(in: NSView?) -> NSPoint](nsgesturerecognizer/location(in:).md)
  Returns the point computed as the location of the gesture.
- [var state: NSGestureRecognizer.State](nsgesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
- [var isEnabled: Bool](nsgesturerecognizer/isenabled.md)
  A Boolean value indicating whether the gesture recognizer is able to handle events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/view)*