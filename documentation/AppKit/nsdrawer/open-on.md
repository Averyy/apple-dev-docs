# open(on:)

**Framework**: AppKit  
**Kind**: method

Causes the receiver to open on the specified edge of the parent window.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func open(on edge: NSRectEdge)
```

## Parameters

- `edge`: The edge of the parent window on which to open the receiver. See Constants for a list of edge constants and locations.

## See Also

- [func close()](nsdrawer/close.md)
  If the receiver is open, this method closes it.
- [func close(Any?)](nsdrawer/close(_:).md)
  An action method to close the receiver.
- [func open()](nsdrawer/open.md)
  If the receiver is closed, this method opens it.
- [func open(Any?)](nsdrawer/open(_:).md)
  An action method to open the drawer.
- [func toggle(Any?)](nsdrawer/toggle(_:).md)
  Toggles the drawer open or closed.
- [var state: Int](nsdrawer/state-swift.property.md)
  The state of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/open(on:))*