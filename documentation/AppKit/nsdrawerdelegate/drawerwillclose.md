# drawerWillClose(_:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate the drawer will close.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func drawerWillClose(_ notification: Notification)
```

## Parameters

- `notification`: An   notification sent by the default notification center immediately before the drawer is closed.

## See Also

- [func drawerShouldOpen(NSDrawer) -> Bool](nsdrawerdelegate/drawershouldopen(_:).md)
  Asks the delegate if the specified drawer should open.
- [func drawerWillOpen(Notification)](nsdrawerdelegate/drawerwillopen(_:).md)
  Notifies the delegate that the drawer will open.
- [func drawerDidOpen(Notification)](nsdrawerdelegate/drawerdidopen(_:).md)
  Notifies the delegate that the drawer has opened.
- [func drawerShouldClose(NSDrawer) -> Bool](nsdrawerdelegate/drawershouldclose(_:).md)
  Asks the delegate if the specified drawer should close.
- [func drawerDidClose(Notification)](nsdrawerdelegate/drawerdidclose(_:).md)
  Notifies the delegate that the drawer has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawerwillclose(_:))*