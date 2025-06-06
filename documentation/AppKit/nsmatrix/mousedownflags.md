# mouseDownFlags

**Framework**: AppKit  
**Kind**: property

The flags in effect at the mouse-down event that started the current tracking session.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var mouseDownFlags: Int { get }
```

#### Discussion

The [`NSMatrix`](nsmatrix.md) [`mouseDown(with:)`](nsmatrix/mousedown(with:).md) method obtains these flags by sending a [`modifierFlags`](nsevent/modifierflags-swift.property.md) message to the event passed into [`mouseDown(with:)`](nsmatrix/mousedown(with:).md). Use this property if you want to access these flags. This property is valid only during tracking; it isn’t useful if the target of the receiver initiates another tracking loop as part of its action method (as a cell that pops up a pop-up list does, for example).

## See Also

- [func sendAction(on: NSEvent.EventTypeMask) -> Int](nscontrol/sendaction(on:).md)
  Sets the conditions on which the receiver sends action messages to its target.
- [func acceptsFirstMouse(for: NSEvent?) -> Bool](nsmatrix/acceptsfirstmouse(for:).md)
  Returns a Boolean value indicating whether the receiver accepts the first mouse.
- [func mouseDown(with: NSEvent)](nsmatrix/mousedown(with:).md)
  Responds to a mouse-down event.
- [func performKeyEquivalent(with: NSEvent) -> Bool](nsmatrix/performkeyequivalent(with:).md)
  Looks for a cell that has the given key equivalent and, if found, makes that cell respond as if clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/mousedownflags)*