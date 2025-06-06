# FIFinderSyncController

**Framework**: Finder Sync  
**Kind**: class

A controller that acts as a bridge between your Finder Sync extension and the Finder itself.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class FIFinderSyncController
```

#### Overview

Use the Finder Sync controller to configure your extension, to set badges on items in the Finder’s window, and to get a list of selected and targeted items.

## Topics

### Managing the Finder Sync Controller
- [class func `default`() -> Self](fifindersynccontroller/default.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](fifindersynccontroller/directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](fifindersynccontroller/selecteditemurls.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](fifindersynccontroller/setbadgeidentifier(_:for:).md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](fifindersynccontroller/setbadgeimage(_:label:forbadgeidentifier:).md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](fifindersynccontroller/targetedurl.md)
  Returns the URL of the Finder’s current target.
### Instance Methods
- [func lastUsedDateForItem(with: URL) -> Date?](fifindersynccontroller/lastuseddateforitem(with:).md)
- [func setLastUsedDate(Date, forItemWith: URL, completion: (any Error) -> Void)](fifindersynccontroller/setlastuseddate(_:foritemwith:completion:).md)
- [func setTagData(Data?, forItemWith: URL, completion: (any Error) -> Void)](fifindersynccontroller/settagdata(_:foritemwith:completion:).md)
- [func tagDataForItem(with: URL) -> Data?](fifindersynccontroller/tagdataforitem(with:).md)
### Type Properties
- [class var isExtensionEnabled: Bool](fifindersynccontroller/isextensionenabled.md)
### Type Methods
- [class func showExtensionManagementInterface()](fifindersynccontroller/showextensionmanagementinterface.md)

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/NSExtensionContext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class FIFinderSync](fifindersync-swift.class.md)
  A type to subclass to add badges, custom shortcut menus, and toolbar buttons to the Finder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller)*