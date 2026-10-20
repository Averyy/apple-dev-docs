# FIFinderSyncProtocol

**Framework**: Finder Sync  
**Kind**: protocol  
**Role**: Protocol

The group of methods to implement for modifying the Finder user interface to express file synchronization status and control.

**Availability**:
- macOS 10.10+

## Declaration

```swift
protocol FIFinderSyncProtocol
```

```objc
@protocol FIFinderSync
```

## Topics

### Managing Badges, Shortcut Menus, and Toolbar Buttons
- [func beginObservingDirectory(at: URL)](./fifindersyncprotocol/beginobservingdirectory%28at%29.md)
  Tells the extension that the user is looking at a monitored directory or at one of its subdirectories.
- [func endObservingDirectory(at: URL)](./fifindersyncprotocol/endobservingdirectory%28at%29.md)
  Tells the extension that the user has stopped looking at a monitored directory or at one of its subdirectories.
- [func menu(for: FIMenuKind) -> NSMenu?](./fifindersyncprotocol/menu%28for%29.md)
  Requests a custom menu from the extension.
- [func requestBadgeIdentifier(for: URL)](./fifindersyncprotocol/requestbadgeidentifier%28for%29.md)
  Requests a badge for the given file or directory.
- [var toolbarItemImage: NSImage](./fifindersyncprotocol/toolbaritemimage.md)
  The image for the extension’s toolbar button.
- [var toolbarItemName: String](./fifindersyncprotocol/toolbaritemname.md)
  The name of the extension’s toolbar button.
- [var toolbarItemToolTip: String](./fifindersyncprotocol/toolbaritemtooltip.md)
  The tooltip text for the extension’s toolbar button.
### Constants
- [enum FIMenuKind](./fimenukind.md)
  The different kinds of custom menus that the Finder Sync extension can provide.
### Instance Methods
- [func makeListenerEndpoint(forServiceName: NSFileProviderServiceName, itemURL: URL) throws -> NSXPCListenerEndpoint](./fifindersyncprotocol/makelistenerendpoint%28forservicename,itemurl%29.md)
- [func supportedServiceNamesForItem(with: URL) -> [NSFileProviderServiceName]](./fifindersyncprotocol/supportedservicenamesforitem%28with%29.md)
- [func values(forAttributes: [URLResourceKey], forItemWith: URL, completion: ([URLResourceKey : Any], (any Error)?) -> Void)](./fifindersyncprotocol/values%28forattributes,foritemwith,completion%29.md)

## Relationships

### Conforming Types
- [FIFinderSync](./fifindersync-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersyncprotocol)*