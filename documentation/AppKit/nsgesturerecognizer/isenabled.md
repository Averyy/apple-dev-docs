# isEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the gesture recognizer is able to handle events.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var isEnabled: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the gesture recognizer receives events and uses them to determine when its gesture is performed. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the gesture recognizer does not receive events. Changing the value from [`true`](https://developer.apple.com/documentation/Swift/true) to [`false`](https://developer.apple.com/documentation/Swift/false) while the gesture recognizer is in the process of recognizing a gesture changes the state of the gesture recognizer to [`NSGestureRecognizer.State.cancelled`](nsgesturerecognizer/state-swift.enum/cancelled.md).

The default value of this property is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var state: NSGestureRecognizer.State](nsgesturerecognizer/state-swift.property.md)
  The current state of the gesture recognizer.
- [var view: NSView?](nsgesturerecognizer/view.md)
  The view to which the gesture recognizer is attached.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/isenabled)*