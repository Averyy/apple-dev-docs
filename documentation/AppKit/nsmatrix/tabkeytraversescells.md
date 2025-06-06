# tabKeyTraversesCells

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether pressing the Tab key advances the key cell to the next selectable cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var tabKeyTraversesCells: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), pressing the Tab key should advance the key cell to the next selectable cell in the receiver. When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false) or if there aren’t any selectable cells after the current one, the next view in the window becomes key when the user presses the Tab key.

Pressing Shift-Tab causes the key cell to advance in the opposite direction (if the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), or if there aren’t any selectable cells before the current one, the previous view in the window becomes key).

## See Also

- [func selectKeyView(following: NSView)](nswindow/selectkeyview(following:).md)
  Gives key view status to the view that follows the given view.
- [var keyCell: NSCell?](nsmatrix/keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func selectNextKeyView(Any?)](nswindow/selectnextkeyview(_:).md)
  Searches for a candidate next key view and, if it finds one, tries to make it the first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/tabkeytraversescells)*