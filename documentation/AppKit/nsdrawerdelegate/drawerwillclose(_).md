# drawerWillClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate the drawer will close.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
optional func drawerWillClose(_ notification: Notification)
```

```objc
- (void) drawerWillClose:(NSNotification *) notification;
```

## Parameters

- `notification`: An [`NSDrawerDelegate`](../nsdrawerdelegate.md) notification sent by the default notification center immediately before the drawer is closed.

## See Also

### Opening and Closing Drawers
- [func drawerShouldOpen(NSDrawer) -> Bool](./drawershouldopen%28_%29.md)
  Asks the delegate if the specified drawer should open.
- [func drawerWillOpen(Notification)](./drawerwillopen%28_%29.md)
  Notifies the delegate that the drawer will open.
- [func drawerDidOpen(Notification)](./drawerdidopen%28_%29.md)
  Notifies the delegate that the drawer has opened.
- [func drawerShouldClose(NSDrawer) -> Bool](./drawershouldclose%28_%29.md)
  Asks the delegate if the specified drawer should close.
- [func drawerDidClose(Notification)](./drawerdidclose%28_%29.md)
  Notifies the delegate that the drawer has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawerwillclose(_:))*