# drawerDidClose(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that the drawer has closed.

**Availability**:
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Drawers are deprecated; consider using NSSplitViewController

## Declaration

```swift
optional func drawerDidClose(_ notification: Notification)
```

```objc
- (void) drawerDidClose:(NSNotification *) notification;
```

## Parameters

- `notification`: An [`NSDrawerDelegate`](../nsdrawerdelegate.md) notification sent by the default notification center immediately after the drawer has closed.

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
- [func drawerWillClose(Notification)](./drawerwillclose%28_%29.md)
  Notifies the delegate the drawer will close.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawerdidclose(_:))*