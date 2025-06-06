# performKeyEquivalent(with:)

**Framework**: AppKit  
**Kind**: method

Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performKeyEquivalent(with event: NSEvent) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if a cell in the receiver responds to the key equivalent in `theEvent`, [`false`](https://developer.apple.com/documentation/swift/false) if no cell responds.

#### Discussion

If there’s a cell in the receiver that has a key equivalent equal to the character in [`theEvent```NSEvent/charactersIgnoringModifiers``] (taking into account any key modifier flags) and that cell is enabled, that cell is made to react as if the user had clicked it: by highlighting, changing its state as appropriate, sending its action if it has one, and then unhighlighting.

Your code should never send this message—it is sent when the receiver or one of its superviews is the first responder and the user presses a key. You may want to override this method to change the way key equivalents are performed or displayed or to disable them in your subclass.

## Parameters

- `event`: The event containing the character for which to find a key equivalent.

## See Also

- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsmatrix/acceptsfirstmouse(for:).md)
  Returns a Boolean value indicating whether the receiver accepts the first mouse.
- [func mouseDown(with: NSEvent)](nsmatrix/mousedown(with:).md)
  Responds to a mouse-down event.
- [var mouseDownFlags: Int](nsmatrix/mousedownflags.md)
  The flags in effect at the mouse-down event that started the current tracking session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/performkeyequivalent(with:))*