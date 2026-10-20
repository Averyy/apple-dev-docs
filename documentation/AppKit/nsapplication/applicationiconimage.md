# applicationIconImage

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The image used for the app’s icon.

**Availability**:
- macOS

## Declaration

```swift
var applicationIconImage: NSImage! { get set }
```

```objc
@property (strong, null_resettable) NSImage * applicationIconImage;
```

#### Discussion

Assign an image to this property when you want to temporarily change the app icon in the dock app tile. The image you provide is scaled as needed so that it fits in the tile. To restore your app’s original icon, set this property to `nil`.

## See Also

### Accessing the dock tile
- [var dockTile: NSDockTile](./docktile.md)
  The app’s Dock tile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/applicationiconimage)*