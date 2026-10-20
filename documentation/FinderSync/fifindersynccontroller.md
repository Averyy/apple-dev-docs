# FIFinderSyncController

**Framework**: Finder Sync  
**Kind**: class  
**Role**: Class

A controller that acts as a bridge between your Finder Sync extension and the Finder itself.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class FIFinderSyncController
```

```objc
@interface FIFinderSyncController : NSExtensionContext
```

#### Overview

Use the Finder Sync controller to configure your extension, to set badges on items in the Finder’s window, and to get a list of selected and targeted items.

## Topics

### Managing the Finder Sync Controller
- [class func `default`() -> Self](./fifindersynccontroller/default%28%29.md)
  Returns the shared Finder Sync controller object.
- [var directoryURLs: Set<URL>!](./fifindersynccontroller/directoryurls.md)
  The directories managed by this extension.
- [func selectedItemURLs() -> [URL]?](./fifindersynccontroller/selecteditemurls%28%29.md)
  Returns an array of selected items.
- [func setBadgeIdentifier(String, for: URL)](./fifindersynccontroller/setbadgeidentifier%28_,for%29.md)
  Sets the badge for a file or directory.
- [func setBadgeImage(NSImage, label: String?, forBadgeIdentifier: String)](./fifindersynccontroller/setbadgeimage%28_,label,forbadgeidentifier%29.md)
  Sets the badge image and label for the given ID.
- [func targetedURL() -> URL?](./fifindersynccontroller/targetedurl%28%29.md)
  Returns the URL of the Finder’s current target.
### Instance Methods
- [func lastUsedDateForItem(with: URL) -> Date?](./fifindersynccontroller/lastuseddateforitem%28with%29.md)
- [func setLastUsedDate(Date, forItemWith: URL, completion: (any Error) -> Void)](./fifindersynccontroller/setlastuseddate%28_,foritemwith,completion%29.md)
- [func setTagData(Data?, forItemWith: URL, completion: (any Error) -> Void)](./fifindersynccontroller/settagdata%28_,foritemwith,completion%29.md)
- [func tagDataForItem(with: URL) -> Data?](./fifindersynccontroller/tagdataforitem%28with%29.md)
### Type Properties
- [class var isExtensionEnabled: Bool](./fifindersynccontroller/isextensionenabled.md)
### Type Methods
- [class func showExtensionManagementInterface()](./fifindersynccontroller/showextensionmanagementinterface%28%29.md)

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/nsextensioncontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class FIFinderSync](./fifindersync-swift.class.md)
  A type to subclass to add badges, custom shortcut menus, and toolbar buttons to the Finder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/findersync/fifindersynccontroller)*