# delegate

**Framework**: AppKit  
**Kind**: property

The window’s delegate.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var delegate: (any NSWindowDelegate)? { get set }
```

#### Discussion

The value of this property is `nil` if the window doesn’t have a delegate.

A window object’s delegate is inserted in the responder chain after the window itself and is informed of various actions by the window through delegation messages.

## See Also

- [func tryToPerform(Selector, with: Any?) -> Bool](nswindow/trytoperform(_:with:).md)
  Dispatches action messages with a given argument.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](nsapplication/sendaction(_:to:from:).md)
  Sends the given action message to the given target.
- [protocol NSWindowDelegate](nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/delegate)*