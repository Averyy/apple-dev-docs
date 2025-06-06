# setDockTile(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Invoked when the plug-in is first loaded and when the application is removed from the Dock.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func setDockTile(_ dockTile: NSDockTile?)
```

#### Discussion

The plugin is loaded in a system process at login time or when the application tile is added to the Dock.

The principal class of the plug-in must implement the `NSDockTilePlugIn` protocol.

## Parameters

- `dockTile`: The dock tile associated with the application, or   if the application has been removed from the Dock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocktileplugin/setdocktile(_:))*