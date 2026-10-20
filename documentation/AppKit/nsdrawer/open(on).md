# open(on:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to open on the specified edge of the parent window.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
func open(on edge: NSRectEdge)
```

```objc
- (void) openOnEdge:(NSRectEdge) edge;
```

## Parameters

- `edge`: The edge of the parent window on which to open the receiver. See Constants for a list of edge constants and locations.

## See Also

### Opening and Closing Drawers
- [func close()](./close%28%29.md)
  If the receiver is open, this method closes it.
- [func close(Any?)](./close%28_%29.md)
  An action method to close the receiver.
- [func open()](./open%28%29.md)
  If the receiver is closed, this method opens it.
- [func open(Any?)](./open%28_%29.md)
  An action method to open the drawer.
- [func toggle(Any?)](./toggle%28_%29.md)
  Toggles the drawer open or closed.
- [var state: Int](./state-swift.property.md)
  The state of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/open(on:))*