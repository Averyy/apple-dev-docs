# delegate

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window’s delegate.

**Availability**:
- macOS

## Declaration

```swift
weak var delegate: (any NSWindowDelegate)? { get set }
```

```objc
@property (weak, nullable) id<NSWindowDelegate> delegate;
```

## Discussion

The value of this property is `nil` if the window doesn’t have a delegate.

A window object’s delegate is inserted in the responder chain after the window itself and is informed of various actions by the window through delegation messages.

## See Also

### Related Documentation
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches action messages with a given argument.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](../nsapplication/sendaction%28_,to,from%29.md)
  Sends the given action message to the given target.
### Managing the Window’s Behavior
- [protocol NSWindowDelegate](../nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/delegate)*