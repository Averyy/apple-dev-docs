# close(_:)

**Framework**: AppKit  
**Kind**: method

An action method to close the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func close(_ sender: Any?)
```

#### Discussion

This method is an action method and likely would not be invoked programatically. Rather, it is an action that is commonly connected in Interface Builder.

## Parameters

- `sender`: A user interface element, such as a button or menu item, that invokes the action method.

## See Also

- [func close()](nsdrawer/close.md)
  If the receiver is open, this method closes it.
- [func open()](nsdrawer/open.md)
  If the receiver is closed, this method opens it.
- [func open(Any?)](nsdrawer/open(_:).md)
  An action method to open the drawer.
- [func open(on: NSRectEdge)](nsdrawer/open(on:).md)
  Causes the receiver to open on the specified edge of the parent window.
- [func toggle(Any?)](nsdrawer/toggle(_:).md)
  Toggles the drawer open or closed.
- [var state: Int](nsdrawer/state-swift.property.md)
  The state of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/close(_:))*