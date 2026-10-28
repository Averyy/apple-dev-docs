# mouseDown(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Responds to a mouse-down event.

**Availability**:
- macOS

## Declaration

```swift
func mouseDown(with event: NSEvent)
```

```objc
- (void) mouseDown:(NSEvent *) event;
```

## Discussion

A mouse-down event in a text cell initiates editing mode. A double click in any cell type except a text cell sends the double-click action of the receiver (if there is one) in addition to the single-click action.

Your code should never invoke this method, but you may override it to implement different mouse tracking than [`NSMatrix`](../nsmatrix.md) does. The response of the receiver depends on its selection mode, as explained in the class description.

## Parameters

- `event`: The mouse-down event.

## See Also

### Related Documentation
- [func sendAction() -> Bool](./sendaction%28%29.md)
  If the selected cell has both an action and a target, sends its action to its target.
- [func sendDoubleAction()](./senddoubleaction%28%29.md)
  Sends the double-click action message to the target of the receiver.
### Handling Event and Action Messages
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](./acceptsfirstmouse%28for%29.md)
  Returns a Boolean value indicating whether the receiver accepts the first mouse.
- [var mouseDownFlags: Int](./mousedownflags.md)
  The flags in effect at the mouse-down event that started the current tracking session.
- [func performKeyEquivalent(with: NSEvent) -> Bool](./performkeyequivalent%28with%29.md)
  Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mousedown(with:))*