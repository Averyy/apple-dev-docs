# open(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

An action method to open the drawer.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
func open(_ sender: Any?)
```

```objc
- (void) open:(id) sender;
```

## Discussion

This method is an action method and likely would not be invoked programatically. Rather, it is an action that is commonly connected in Interface Builder.

## Parameters

- `sender`: A user interface element, such as a button or menu item, that invokes the action method.

## See Also

### Opening and Closing Drawers
- [func close()](./close%28%29.md)
  If the receiver is open, this method closes it.
- [func close(Any?)](./close%28_%29.md)
  An action method to close the receiver.
- [func open()](./open%28%29.md)
  If the receiver is closed, this method opens it.
- [func open(on: NSRectEdge)](./open%28on%29.md)
  Causes the receiver to open on the specified edge of the parent window.
- [func toggle(Any?)](./toggle%28_%29.md)
  Toggles the drawer open or closed.
- [var state: Int](./state-swift.property.md)
  The state of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawer/open(_:))*