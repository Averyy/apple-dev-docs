# drawerShouldOpen(_:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate if the specified drawer should open.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func drawerShouldOpen(_ sender: NSDrawer) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the drawer should open; [`false`](https://developer.apple.com/documentation/swift/false) to prevent the drawer from opening.

#### Discussion

This method is invoked on user-initiated attempts to open a drawer by dragging it or when the [`NSDrawerDelegate`](nsdrawerdelegate.md) method is called.

## Parameters

- `sender`: The drawer requesting permission to open.

## See Also

- [Drawer Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Drawers/Drawers.html#//apple_ref/doc/uid/10000001i)
- [func drawerWillOpen(Notification)](nsdrawerdelegate/drawerwillopen(_:).md)
  Notifies the delegate that the drawer will open.
- [func drawerDidOpen(Notification)](nsdrawerdelegate/drawerdidopen(_:).md)
  Notifies the delegate that the drawer has opened.
- [func drawerShouldClose(NSDrawer) -> Bool](nsdrawerdelegate/drawershouldclose(_:).md)
  Asks the delegate if the specified drawer should close.
- [func drawerWillClose(Notification)](nsdrawerdelegate/drawerwillclose(_:).md)
  Notifies the delegate the drawer will close.
- [func drawerDidClose(Notification)](nsdrawerdelegate/drawerdidclose(_:).md)
  Notifies the delegate that the drawer has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawershouldopen(_:))*