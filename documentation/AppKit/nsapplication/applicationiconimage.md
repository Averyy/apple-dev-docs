# applicationIconImage

**Framework**: AppKit  
**Kind**: property

The image used for the app’s icon.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var applicationIconImage: NSImage! { get set }
```

#### Discussion

Assign an image to this property when you want to temporarily change the app icon in the dock app tile. The image you provide is scaled as needed so that it fits in the tile. To restore your app’s original icon, set this property to `nil`.

## See Also

- [var dockTile: NSDockTile](nsapplication/docktile.md)
  The app’s Dock tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/applicationiconimage)*