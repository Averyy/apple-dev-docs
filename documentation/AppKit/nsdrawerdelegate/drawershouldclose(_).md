# drawerShouldClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the specified drawer should close.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
optional func drawerShouldClose(_ sender: NSDrawer) -> Bool
```

```objc
- (BOOL) drawerShouldClose:(NSDrawer *) sender;
```

#### Return Value

[`true`](../../Swift/true.md) to allow the drawer to close; [`false`](../../Swift/false.md) to prevent it from closing.

#### Discussion

This method is invoked on user-initiated attempts to close a drawer by dragging it or when the [`NSDrawerDelegate`](../nsdrawerdelegate.md) method is called.

## Parameters

- `sender`: The drawer being closed.

## See Also

### Opening and Closing Drawers
- [func drawerShouldOpen(NSDrawer) -> Bool](./drawershouldopen%28_%29.md)
  Asks the delegate if the specified drawer should open.
- [func drawerWillOpen(Notification)](./drawerwillopen%28_%29.md)
  Notifies the delegate that the drawer will open.
- [func drawerDidOpen(Notification)](./drawerdidopen%28_%29.md)
  Notifies the delegate that the drawer has opened.
- [func drawerWillClose(Notification)](./drawerwillclose%28_%29.md)
  Notifies the delegate the drawer will close.
- [func drawerDidClose(Notification)](./drawerdidclose%28_%29.md)
  Notifies the delegate that the drawer has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawershouldclose(_:))*