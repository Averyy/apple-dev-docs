# toolbarItemToolTip

**Framework**: Finder Sync  
**Kind**: property  
**Role**: Instance Property

The tooltip text for the extension’s toolbar button.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional var toolbarItemToolTip: String { get }
```

```objc
@property (copy, readonly) NSString * toolbarItemToolTip;
```

## Discussion

To add a toolbar item to the Finder, override the getter method for the toolbar image, name, and tooltip properties.

## See Also

### Managing Badges, Shortcut Menus, and Toolbar Buttons
- [func beginObservingDirectory(at: URL)](./beginobservingdirectory%28at%29.md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func endObservingDirectory(at: URL)](./endobservingdirectory%28at%29.md)
  Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.
- [func menu(for: FIMenuKind) -> NSMenu?](./menu%28for%29.md)
  Requests a custom menu from the extension.
- [func requestBadgeIdentifier(for: URL)](./requestbadgeidentifier%28for%29.md)
  Requests a badge for the given file or directory.
- [var toolbarItemImage: NSImage](./toolbaritemimage.md)
  The image for the extension’s toolbar button.
- [var toolbarItemName: String](./toolbaritemname.md)
  The name of the extension’s toolbar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/toolbaritemtooltip)*