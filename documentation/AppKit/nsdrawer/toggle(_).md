# toggle(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Toggles the drawer open or closed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
func toggle(_ sender: Any?)
```

```objc
- (void) toggle:(id) sender;
```

## Discussion

If the receiver is closed, or in the process of either opening or closing, it is opened. Otherwise, the drawer is closed.

## Parameters

- `sender`: The sender of the message.

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
- [func open(on: NSRectEdge)](./open%28on%29.md)
  Causes the receiver to open on the specified edge of the parent window.
- [var state: Int](./state-swift.property.md)
  The state of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/toggle(_:))*