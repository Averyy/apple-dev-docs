# NSFileProviderItemIdentifier

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

A unique identifier for an item managed by the File Provider extension.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderItemIdentifier
```

```c
typedef NSString * NSFileProviderItemIdentifier;
```

## Topics

### Constants
- [static let rootContainer: NSFileProviderItemIdentifier](./nsfileprovideritemidentifier/rootcontainer.md)
  The persistent identifier for the root directory of the file provider’s shared file hierarchy.
- [static let workingSet: NSFileProviderItemIdentifier](./nsfileprovideritemidentifier/workingset.md)
  The persistent identifier representing the working set of documents and directories.
- [static let trashContainer: NSFileProviderItemIdentifier](./nsfileprovideritemidentifier/trashcontainer.md)
  The persistent identifier for the parent of all trashed items.
### Initializers
- [init(String)](./nsfileprovideritemidentifier/init%28_%29.md)
  Returns a newly instantiated persistent identifier.
- [init(rawValue: String)](./nsfileprovideritemidentifier/init%28rawvalue%29.md)
  Returns a newly instantiated persistent identifier.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Provided items
- [typealias NSFileProviderItem](./nsfileprovideritem-swift.typealias.md)
  An item the File Provider extension manages.
- [protocol NSFileProviderItemProtocol](./nsfileprovideritemprotocol.md)
  A protocol that defines the properties of an item managed by the File Provider extension.
- [struct NSFileProviderItemCapabilities](./nsfileprovideritemcapabilities.md)
  An item’s capabilities, which define the actions that the user can perform in the document browser.
- [struct NSFileProviderTypeAndCreator](./nsfileprovidertypeandcreator.md)
  A structure that contains the file type and file creator codes for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemidentifier)*