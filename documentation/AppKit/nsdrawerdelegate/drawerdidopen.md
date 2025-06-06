# drawerDidOpen(_:)

**Framework**: AppKit  
**Kind**: method

Notifies the delegate that the drawer has opened.

**Availability**:
- macOS 10.0+

## Declaration

```swift
optional func drawerDidOpen(_ notification: Notification)
```

## Parameters

- `notification`: An   notification, sent by the default notification center immediately after the drawer has opened.

## See Also

- [func drawerShouldOpen(NSDrawer) -> Bool](nsdrawerdelegate/drawershouldopen(_:).md)
  Asks the delegate if the specified drawer should open.
- [func drawerWillOpen(Notification)](nsdrawerdelegate/drawerwillopen(_:).md)
  Notifies the delegate that the drawer will open.
- [func drawerShouldClose(NSDrawer) -> Bool](nsdrawerdelegate/drawershouldclose(_:).md)
  Asks the delegate if the specified drawer should close.
- [func drawerWillClose(Notification)](nsdrawerdelegate/drawerwillclose(_:).md)
  Notifies the delegate the drawer will close.
- [func drawerDidClose(Notification)](nsdrawerdelegate/drawerdidclose(_:).md)
  Notifies the delegate that the drawer has closed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate/drawerdidopen(_:))*