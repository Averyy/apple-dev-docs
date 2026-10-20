# state

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The state of the receiver.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
var state: Int { get }
```

```objc
@property (readonly) NSInteger state;
```

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
- [func toggle(Any?)](./toggle%28_%29.md)
  Toggles the drawer open or closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/state-swift.property)*