# requestBadgeIdentifier(for:)

**Framework**: Finder Sync  
**Kind**: method

Requests a badge for the given file or directory.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func requestBadgeIdentifier(for url: URL)
```

#### Discussion

Override this method to receive notifications whenever a new item becomes visible in the Finder. Check the item’s state, and call [`setBadgeIdentifier(_:for:)`](fifindersynccontroller/setbadgeidentifier(_:for:).md) to set an appropriate badge.

## Parameters

- `url`: The URL of a file or directory inside the extension’s monitored   directories.

## See Also

- [func setBadgeIdentifier(String, for: URL)](fifindersynccontroller/setbadgeidentifier(_:for:).md)
  Sets the badge for a file or directory.
- [func beginObservingDirectory(at: URL)](fifindersyncprotocol/beginobservingdirectory(at:).md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func endObservingDirectory(at: URL)](fifindersyncprotocol/endobservingdirectory(at:).md)
  Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.
- [func menu(for: FIMenuKind) -> NSMenu?](fifindersyncprotocol/menu(for:).md)
  Requests a custom menu from the extension.
- [var toolbarItemImage: NSImage](fifindersyncprotocol/toolbaritemimage.md)
  The image for the extension’s toolbar button.
- [var toolbarItemName: String](fifindersyncprotocol/toolbaritemname.md)
  The name of the extension’s toolbar button.
- [var toolbarItemToolTip: String](fifindersyncprotocol/toolbaritemtooltip.md)
  The tooltip text for the extension’s toolbar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/requestbadgeidentifier(for:))*