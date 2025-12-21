# NSDrawerDelegate

**Framework**: AppKit  
**Kind**: protocol

A set of methods that drawer delegates implement to open, close, and resize the drawer.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSDrawerDelegate : NSObjectProtocol
```

## Topics

### Opening and Closing Drawers
- [func drawerShouldOpen(NSDrawer) -> Bool](nsdrawerdelegate/drawershouldopen(_:).md)
  Asks the delegate if the specified drawer should open.
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
### Managing Drawer Size
- [func drawerWillResizeContents(NSDrawer, to: NSSize) -> NSSize](nsdrawerdelegate/drawerwillresizecontents(_:to:).md)
  Invoked when the user resizes the drawer or parent.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [NSAccessibility](nsaccessibility.md)
  A legacy, informal protocol that Apple doesn’t recommend for active use.
- [protocol NSEditorRegistration](nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.
- [protocol NSInputServiceProvider](nsinputserviceprovider.md)
- [protocol NSInputServerMouseTracker](nsinputservermousetracker.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate)*