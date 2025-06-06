# NSDockTile

**Framework**: AppKit  
**Kind**: class

The visual representation of your app’s miniaturized windows and app icon as they appear in the Dock.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class NSDockTile
```

#### Overview

You do not create Dock tile objects explicitly in your app. Instead, you retrieve the Dock tile for an existing window or for the app by calling that object’s [`dockTile`](nswindow/docktile.md) method. Also, you do not subclass the [`NSDockTile`](nsdocktile.md) class; instead, you use the methods of the class to make the following customizations:

- Badge the tile with a custom string.
- Remove or show the application icon badge.
- Draw the tile content yourself.

If you decide to draw the tile content yourself, you must provide a custom content view to handle the drawing.

##### Application Dock Tiles

An application Dock tile defaults to display the application’s [`applicationIconImage`](nsapplication/applicationiconimage.md).

The application Dock tile never shows a smaller application icon badge.

Whether using the default or custom view, the application Dock tile may be badged with a short custom string.

##### Window Dock Tiles

A window Dock tile defaults to display a miniaturized version of the windows contents with a badge derived from the application Dock icon, including any customized application Dock icon. The default window Dock tile image may not be badged with a custom string.

A window Dock tile can use a custom view to draw the Dock icon. If a custom view is used, no application badge will be added, but the text label will be overlaid on top of the icon.

## Topics

### Drawing the Tile’s Content
- [var contentView: NSView?](nsdocktile/contentview.md)
  The view to use for drawing the dock tile contents.
### Getting the Tile Information
- [var size: NSSize](nsdocktile/size.md)
  The size of the tile.
- [var owner: AnyObject?](nsdocktile/owner.md)
  The object represented by the dock tile.
### Applying Badge Icons to the Tile
- [var showsApplicationBadge: Bool](nsdocktile/showsapplicationbadge.md)
  A Boolean showing whether the tile is badged with the application’s icon
- [var badgeLabel: String?](nsdocktile/badgelabel.md)
  The string to be displayed in the tile’s badging area.
### Updating the Dock Tile
- [func display()](nsdocktile/display.md)
  Redraws the dock tile’s content.
### Constants
- [Dock Tile Plug-In Support Version](dock-tile-plug-in-support-version.md)
  The version of the AppKit framework containing support for dock tile plug-ins.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSDockTilePlugIn](nsdocktileplugin.md)
  A set of methods implemented by plug-ins that allow an app’s Dock tile to be customized while the app is not running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocktile)*