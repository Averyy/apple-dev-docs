# state

**Framework**: AppKit  
**Kind**: property

The state of the receiver.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var state: Int { get }
```

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
- [func toggle(Any?)](nsdrawer/toggle(_:).md)
  Toggles the drawer open or closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/state-swift.property)*