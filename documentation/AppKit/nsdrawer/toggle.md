# toggle(_:)

**Framework**: AppKit  
**Kind**: method

Toggles the drawer open or closed.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func toggle(_ sender: Any?)
```

#### Discussion

If the receiver is closed, or in the process of either opening or closing, it is opened. Otherwise, the drawer is closed.

## Parameters

- `sender`: The sender of the message.

## See Also

- [func close()](nsdrawer/close.md)
  If the receiver is open, this method closes it.
- [func close(Any?)](nsdrawer/close(_:).md)
  An action method to close the receiver.
- [func open()](nsdrawer/open.md)
  If the receiver is closed, this method opens it.
- [func open(Any?)](nsdrawer/open(_:).md)
  An action method to open the drawer.
- [func open(on: NSRectEdge)](nsdrawer/open(on:).md)
  Causes the receiver to open on the specified edge of the parent window.
- [var state: Int](nsdrawer/state-swift.property.md)
  The state of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/toggle(_:))*