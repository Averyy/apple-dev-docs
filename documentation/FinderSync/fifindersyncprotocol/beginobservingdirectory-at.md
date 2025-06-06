# beginObservingDirectory(at:)

**Framework**: Findersync  
**Kind**: method

Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func beginObservingDirectory(at url: URL)
```

#### Discussion

Override this method to receive notifications when the user opens the contents of a monitored directory or one of its subdirectories in the Finder. The system calls `beginObservingDirectoryAtURL:` only once for each unique URL. As long as the content remains visible in at least one Finder window, any additional Finder windows that open to the same URL are ignored.

> **Note**: The system creates additional instances of your extension for any Open and Save dialogs. These extensions receive their own calls to `beginObservingDirectoryAtURL:`, even if the directory is already open in a Finder window.

## Parameters

- `url`: The URL of the directory.

## See Also

- [func endObservingDirectory(at: URL)](fifindersyncprotocol/endobservingdirectory(at:).md)
  Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.
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

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/beginobservingdirectory(at:))*