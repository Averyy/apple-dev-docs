# endObservingDirectory(at:)

**Framework**: Finder Sync  
**Kind**: method

Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func endObservingDirectory(at url: URL)
```

#### Discussion

Override this method to receive notifications when the user is no longer looking at the contents of the given URL. As with [`beginObservingDirectory(at:)`](fifindersyncprotocol/beginobservingdirectory(at:).md), the Open and Save dialogs are tracked separately from the Finder.

## Parameters

- `url`: The URL of the directory.

## See Also

- [func beginObservingDirectory(at: URL)](fifindersyncprotocol/beginobservingdirectory(at:).md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func menu(for: FIMenuKind) -> NSMenu?](fifindersyncprotocol/menu(for:).md)
  Requests a custom menu from the extension.
- [func requestBadgeIdentifier(for: URL)](fifindersyncprotocol/requestbadgeidentifier(for:).md)
  Requests a badge for the given file or directory.
- [var toolbarItemImage: NSImage](fifindersyncprotocol/toolbaritemimage.md)
  The image for the extension’s toolbar button.
- [var toolbarItemName: String](fifindersyncprotocol/toolbaritemname.md)
  The name of the extension’s toolbar button.
- [var toolbarItemToolTip: String](fifindersyncprotocol/toolbaritemtooltip.md)
  The tooltip text for the extension’s toolbar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/endobservingdirectory(at:))*