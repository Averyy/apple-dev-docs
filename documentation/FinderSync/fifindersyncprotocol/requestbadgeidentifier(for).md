# requestBadgeIdentifier(for:)

**Framework**: Finder Sync  
**Kind**: method  
**Role**: Instance Method

Requests a badge for the given file or directory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func requestBadgeIdentifier(for url: URL)
```

```objc
- (void) requestBadgeIdentifierForURL:(NSURL *) url;
```

## Discussion

Override this method to receive notifications whenever a new item becomes visible in the Finder. Check the item’s state, and call [`setBadgeIdentifier(_:for:)`](../fifindersynccontroller/setbadgeidentifier%28_,for%29.md) to set an appropriate badge.

## Parameters

- `url`: The URL of a file or directory inside the extension’s monitored directories.

## See Also

### Related Documentation
- [func setBadgeIdentifier(String, for: URL)](../fifindersynccontroller/setbadgeidentifier%28_,for%29.md)
  Sets the badge for a file or directory.
### Managing Badges, Shortcut Menus, and Toolbar Buttons
- [func beginObservingDirectory(at: URL)](./beginobservingdirectory%28at%29.md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func endObservingDirectory(at: URL)](./endobservingdirectory%28at%29.md)
  Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.
- [func menu(for: FIMenuKind) -> NSMenu?](./menu%28for%29.md)
  Requests a custom menu from the extension.
- [var toolbarItemImage: NSImage](./toolbaritemimage.md)
  The image for the extension’s toolbar button.
- [var toolbarItemName: String](./toolbaritemname.md)
  The name of the extension’s toolbar button.
- [var toolbarItemToolTip: String](./toolbaritemtooltip.md)
  The tooltip text for the extension’s toolbar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/requestbadgeidentifier(for:))*