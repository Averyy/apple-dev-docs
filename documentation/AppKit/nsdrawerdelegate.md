# NSDrawerDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

A set of methods that drawer delegates implement to open, close, and resize the drawer.

**Availability**:
- macOS

> **Deprecated**: Drawers are deprecated and should not be used in modern macOS apps.

## Declaration

```swift
protocol NSDrawerDelegate : NSObjectProtocol
```

```objc
@protocol NSDrawerDelegate <NSObject>
```

## Topics

### Opening and Closing Drawers
- [func drawerShouldOpen(NSDrawer) -> Bool](./nsdrawerdelegate/drawershouldopen%28_%29.md)
  Asks the delegate if the specified drawer should open.
- [func drawerWillOpen(Notification)](./nsdrawerdelegate/drawerwillopen%28_%29.md)
  Notifies the delegate that the drawer will open.
- [func drawerDidOpen(Notification)](./nsdrawerdelegate/drawerdidopen%28_%29.md)
  Notifies the delegate that the drawer has opened.
- [func drawerShouldClose(NSDrawer) -> Bool](./nsdrawerdelegate/drawershouldclose%28_%29.md)
  Asks the delegate if the specified drawer should close.
- [func drawerWillClose(Notification)](./nsdrawerdelegate/drawerwillclose%28_%29.md)
  Notifies the delegate the drawer will close.
- [func drawerDidClose(Notification)](./nsdrawerdelegate/drawerdidclose%28_%29.md)
  Notifies the delegate that the drawer has closed.
### Managing Drawer Size
- [func drawerWillResizeContents(NSDrawer, to: NSSize) -> NSSize](./nsdrawerdelegate/drawerwillresizecontents%28_,to%29.md)
  Invoked when the user resizes the drawer or parent.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Deprecated protocols
- [NSAccessibility](./nsaccessibility.md)
  A legacy, informal protocol that Apple doesn’t recommend for active use.
- [protocol NSEditorRegistration](./nseditorregistration.md)
  A set of methods that controllers can implement to enable an editor view to inform the controller when it has uncommitted changes.
- [protocol NSInputServiceProvider](./nsinputserviceprovider.md)
- [protocol NSInputServerMouseTracker](./nsinputservermousetracker.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdrawerdelegate)*