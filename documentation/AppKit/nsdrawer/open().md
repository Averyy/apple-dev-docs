# open()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

If the receiver is closed, this method opens it.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
func open()
```

```objc
- (void) open;
```

## Discussion

Calling `open` on an open drawer does nothing. You can get the state of a drawer by sending it [`state`](./state-swift.property.md). If an edge is not specified, an attempt will be made to choose an edge based on the space available to display the drawer onscreen. If you need to ensure that a drawer opens on a particular edge, use [`open(on:)`](./open%28on%29.md).

## See Also

### Opening and Closing Drawers
- [func close()](./close%28%29.md)
  If the receiver is open, this method closes it.
- [func close(Any?)](./close%28_%29.md)
  An action method to close the receiver.
- [func open(Any?)](./open%28_%29.md)
  An action method to open the drawer.
- [func open(on: NSRectEdge)](./open%28on%29.md)
  Causes the receiver to open on the specified edge of the parent window.
- [func toggle(Any?)](./toggle%28_%29.md)
  Toggles the drawer open or closed.
- [var state: Int](./state-swift.property.md)
  The state of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/open())*