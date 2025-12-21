# drawerShouldClose(_:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate if the specified drawer should close.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func drawerShouldClose(_ sender: NSDrawer) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the drawer to close; [`false`](https://developer.apple.com/documentation/Swift/false) to prevent it from closing.

#### Discussion

This method is invoked on user-initiated attempts to close a drawer by dragging it or when the [`NSDrawerDelegate`](nsdrawerdelegate.md) method is called.

## Parameters

- `sender`: The drawer being closed.

## See Also

- [func drawerShouldOpen(NSDrawer) -> Bool](nsdrawerdelegate/drawershouldopen(_:).md)
  Asks the delegate if the specified drawer should open.
- [func drawerWillOpen(Notification)](nsdrawerdelegate/drawerwillopen(_:).md)
  Notifies the delegate that the drawer will open.
- [func drawerDidOpen(Notification)](nsdrawerdelegate/drawerdidopen(_:).md)
  Notifies the delegate that the drawer has opened.
- [func drawerWillClose(Notification)](nsdrawerdelegate/drawerwillclose(_:).md)
  Notifies the delegate the drawer will close.
- [func drawerDidClose(Notification)](nsdrawerdelegate/drawerdidclose(_:).md)
  Notifies the delegate that the drawer has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawershouldclose(_:))*