# mouseDown(with:)

**Framework**: AppKit  
**Kind**: method

Responds to a mouse-down event.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func mouseDown(with event: NSEvent)
```

#### Discussion

A mouse-down event in a text cell initiates editing mode. A double click in any cell type except a text cell sends the double-click action of the receiver (if there is one) in addition to the single-click action.

Your code should never invoke this method, but you may override it to implement different mouse tracking than [`NSMatrix`](nsmatrix.md) does. The response of the receiver depends on its selection mode, as explained in the class description.

## Parameters

- `event`: The mouse-down event.

## See Also

- [func sendAction() -> Bool](nsmatrix/sendaction.md)
  If the selected cell has both an action and a target, sends its action to its target.
- [func sendDoubleAction()](nsmatrix/senddoubleaction.md)
  Sends the double-click action message to the target of the receiver.
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsmatrix/acceptsfirstmouse(for:).md)
  Returns a Boolean value indicating whether the receiver accepts the first mouse.
- [var mouseDownFlags: Int](nsmatrix/mousedownflags.md)
  The flags in effect at the mouse-down event that started the current tracking session.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsmatrix/performkeyequivalent(with:).md)
  Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mousedown(with:))*