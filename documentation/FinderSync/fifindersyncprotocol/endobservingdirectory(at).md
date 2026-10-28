# endObservingDirectory(at:)

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func endObservingDirectory(at url: URL)
```

```objc
- (void) endObservingDirectoryAtURL:(NSURL *) url;
```

## Discussion

Override this method to receive notifications when the user is no longer looking at the contents of the given URL. As with [`beginObservingDirectory(at:)`](./beginobservingdirectory%28at%29.md), the Open and Save dialogs are tracked separately from the Finder.

## Parameters

- `url`: The URL of the directory.

## See Also

### Managing Badges, Shortcut Menus, and Toolbar Buttons
- [func beginObservingDirectory(at: URL)](./beginobservingdirectory%28at%29.md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func menu(for: FIMenuKind) -> NSMenu?](./menu%28for%29.md)
  Requests a custom menu from the extension.
- [func requestBadgeIdentifier(for: URL)](./requestbadgeidentifier%28for%29.md)
  Requests a badge for the given file or directory.
- [var toolbarItemImage: NSImage](./toolbaritemimage.md)
  The image for the extension’s toolbar button.
- [var toolbarItemName: String](./toolbaritemname.md)
  The name of the extension’s toolbar button.
- [var toolbarItemToolTip: String](./toolbaritemtooltip.md)
  The tooltip text for the extension’s toolbar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/endobservingdirectory(at:))*