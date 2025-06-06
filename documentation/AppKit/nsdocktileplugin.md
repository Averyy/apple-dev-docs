# NSDockTilePlugIn

**Framework**: AppKit  
**Kind**: protocol

A set of methods implemented by plug-ins that allow an app’s Dock tile to be customized while the app is not running.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSDockTilePlugIn : NSObjectProtocol
```

#### Overview

Customizing an application’s Dock tile when the application itself is not running requires that you write a plug-in. The plug-in’s principal class must implement the [`NSDockTilePlugIn`](nsdocktileplugin.md) protocol.

The name of the plugin is indicated by a `NSDockTilePlugIn` key in the application’s `Info.plist` file.

The plugin is loaded in a system process at login time or when the application tile is added to the Dock.  When the plugin is loaded, the principal class’ implementation of [`setDockTile(_:)`](nsdocktileplugin/setdocktile(_:).md) is invoked, passing an [`NSDockTile`](nsdocktile.md) for the plug-in to customize.  If the principal class implements [`dockMenu()`](nsdocktileplugin/dockmenu().md) it is invoked whenever the user causes the application’s dock menu to be shown.  When the dock tile is no longer valid (for example,. the application has been removed from the dock) -[`setDockTile(_:)`](nsdocktileplugin/setdocktile(_:).md) is invoked with `nil`.

## Topics

### Setting the Dock Tile
- [func setDockTile(NSDockTile?)](nsdocktileplugin/setdocktile(_:).md)
  Invoked when the plug-in is first loaded and when the application is removed from the Dock.
### Getting the Dock Tile Menu
- [func dockMenu() -> NSMenu?](nsdocktileplugin/dockmenu.md)
  Invoked when the user causes the application’s dock menu to be shown.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSDockTile](nsdocktile.md)
  The visual representation of your app’s miniaturized windows and app icon as they appear in the Dock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocktileplugin)*