# menu(for:)

**Framework**: Finder Sync  
**Kind**: method

Requests a custom menu from the extension.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func menu(for menu: FIMenuKind) -> NSMenu?
```

#### Return Value

A custom menu.

#### Discussion

Override this method to provide custom menus in the Finder. You can customize this menu based both on the menu’s kind and on the selected and targeted items (if any). You can get the selected and targeted items from the extension’s [`FIFinderSyncController`](fifindersynccontroller.md).

If `kind` is `FIMenuKindToolbarItemMenu`, the system always calls this method even if the target and selection are not related to the extension.

The extension’s principal object provides a method for each menu item’s assigned action.

## Parameters

- `menu`: The type of menu being displayed. For a list of possible values, see  .

## See Also

- [func targetedURL() -> URL?](fifindersynccontroller/targetedurl.md)
  Returns the URL of the Finder’s current target.
- [func selectedItemURLs() -> [URL]?](fifindersynccontroller/selecteditemurls.md)
  Returns an array of selected items.
- [func beginObservingDirectory(at: URL)](fifindersyncprotocol/beginobservingdirectory(at:).md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func endObservingDirectory(at: URL)](fifindersyncprotocol/endobservingdirectory(at:).md)
  Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.
- [func requestBadgeIdentifier(for: URL)](fifindersyncprotocol/requestbadgeidentifier(for:).md)
  Requests a badge for the given file or directory.
- [var toolbarItemImage: NSImage](fifindersyncprotocol/toolbaritemimage.md)
  The image for the extension’s toolbar button.
- [var toolbarItemName: String](fifindersyncprotocol/toolbaritemname.md)
  The name of the extension’s toolbar button.
- [var toolbarItemToolTip: String](fifindersyncprotocol/toolbaritemtooltip.md)
  The tooltip text for the extension’s toolbar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/menu(for:))*