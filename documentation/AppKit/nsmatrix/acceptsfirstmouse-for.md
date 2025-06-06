# acceptsFirstMouse(for:)

**Framework**: AppKit  
**Kind**: method

Returns a Boolean value indicating whether the receiver accepts the first mouse.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func acceptsFirstMouse(for event: NSEvent?) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/swift/false) if the selection mode of the receiver is `NSListModeMatrix`, [`true`](https://developer.apple.com/documentation/swift/true) if the receiver is in any other selection mode. The receiver does not accept first mouse in `NSListModeMatrix` to prevent the loss of multiple selections.

## Parameters

- `event`: This parameter is ignored.

## See Also

- [var mode: NSMatrix.Mode](nsmatrix/mode-swift.property.md)
  The selection mode of the receiver.
- [func mouseDown(with: NSEvent)](nsmatrix/mousedown(with:).md)
  Responds to a mouse-down event.
- [var mouseDownFlags: Int](nsmatrix/mousedownflags.md)
  The flags in effect at the mouse-down event that started the current tracking session.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsmatrix/performkeyequivalent(with:).md)
  Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/acceptsfirstmouse(for:))*