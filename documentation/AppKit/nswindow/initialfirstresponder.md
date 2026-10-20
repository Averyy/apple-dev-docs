# initialFirstResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The view that’s made first responder (also called the key view) the first time the window is placed onscreen.

**Availability**:
- macOS

## Declaration

```swift
weak var initialFirstResponder: NSView? { get set }
```

```objc
@property (weak, nullable) NSView * initialFirstResponder;
```

## See Also

### Related Documentation
- [var nextKeyView: NSView?](../nsview/nextkeyview.md)
  The view object that follows the current view in the key view loop.
### Managing Responders
- [var firstResponder: NSResponder?](./firstresponder.md)
  The window’s first responder.
- [func makeFirstResponder(NSResponder?) -> Bool](./makefirstresponder%28_%29.md)
  Attempts to make a given responder the first responder for the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/initialfirstresponder)*