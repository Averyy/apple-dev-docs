# previousValidKeyView

**Framework**: AppKit  
**Kind**: property

The closest view object in the key view loop that precedes the current view and accepts first responder status.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var previousValidKeyView: NSView? { get }
```

#### Discussion

The value in this property is `nil` if there is no view that precedes the current view and accepts the first responder status. AppKit ignores hidden views when it determines the previous valid key view.

## See Also

- [func selectKeyView(following: NSView)](nswindow/selectkeyview(following:).md)
  Gives key view status to the view that follows the given view.
- [var isHidden: Bool](nsview/ishidden.md)
  A Boolean value indicating whether the view is hidden.
- [func selectNextKeyView(Any?)](nswindow/selectnextkeyview(_:).md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.
- [func selectPreviousKeyView(Any?)](nswindow/selectpreviouskeyview(_:).md)
  Searches for a candidate previous key view and, if it finds one, tries to make it the first responder.
- [func selectKeyView(preceding: NSView)](nswindow/selectkeyview(preceding:).md)
  Gives key view status to the view that precedes the given view.
- [var canBecomeKeyView: Bool](nsview/canbecomekeyview.md)
  A Boolean value indicating whether the view can become key view.
- [var needsPanelToBecomeKey: Bool](nsview/needspaneltobecomekey.md)
  A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.
- [var nextKeyView: NSView?](nsview/nextkeyview.md)
  The view object that follows the current view in the key view loop.
- [var nextValidKeyView: NSView?](nsview/nextvalidkeyview.md)
  The closest view object in the key view loop that follows the current view in the key view loop and accepts first responder status.
- [var previousKeyView: NSView?](nsview/previouskeyview.md)
  The view object preceding the current view in the key view loop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/previousvalidkeyview)*