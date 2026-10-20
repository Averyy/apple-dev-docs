# drawerShouldOpen(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the specified drawer should open.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
optional func drawerShouldOpen(_ sender: NSDrawer) -> Bool
```

```objc
- (BOOL) drawerShouldOpen:(NSDrawer *) sender;
```

#### Return Value

[`true`](../../Swift/true.md) if the drawer should open; [`false`](../../Swift/false.md) to prevent the drawer from opening.

#### Discussion

This method is invoked on user-initiated attempts to open a drawer by dragging it or when the [`NSDrawerDelegate`](../nsdrawerdelegate.md) method is called.

## Parameters

- `sender`: The drawer requesting permission to open.

## See Also

### Related Documentation
- [Drawer Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Drawers/Drawers.html#//apple_ref/doc/uid/10000001i)
### Opening and Closing Drawers
- [func drawerWillOpen(Notification)](./drawerwillopen%28_%29.md)
  Notifies the delegate that the drawer will open.
- [func drawerDidOpen(Notification)](./drawerdidopen%28_%29.md)
  Notifies the delegate that the drawer has opened.
- [func drawerShouldClose(NSDrawer) -> Bool](./drawershouldclose%28_%29.md)
  Asks the delegate if the specified drawer should close.
- [func drawerWillClose(Notification)](./drawerwillclose%28_%29.md)
  Notifies the delegate the drawer will close.
- [func drawerDidClose(Notification)](./drawerdidclose%28_%29.md)
  Notifies the delegate that the drawer has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawershouldopen(_:))*