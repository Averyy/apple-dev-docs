# toolbarItemImage

**Framework**: Finder Sync  
**Kind**: property

The image for the extension’s toolbar button.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@NSCopying
optional var toolbarItemImage: NSImage { get }
```

#### Discussion

To add a toolbar item to the Finder, override the getter method for the toolbar image, name, and tooltip properties.

## See Also

- [func beginObservingDirectory(at: URL)](fifindersyncprotocol/beginobservingdirectory(at:).md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func endObservingDirectory(at: URL)](fifindersyncprotocol/endobservingdirectory(at:).md)
  Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.
- [func menu(for: FIMenuKind) -> NSMenu?](fifindersyncprotocol/menu(for:).md)
  Requests a custom menu from the extension.
- [func requestBadgeIdentifier(for: URL)](fifindersyncprotocol/requestbadgeidentifier(for:).md)
  Requests a badge for the given file or directory.
- [var toolbarItemName: String](fifindersyncprotocol/toolbaritemname.md)
  The name of the extension’s toolbar button.
- [var toolbarItemToolTip: String](fifindersyncprotocol/toolbaritemtooltip.md)
  The tooltip text for the extension’s toolbar button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol/toolbaritemimage)*