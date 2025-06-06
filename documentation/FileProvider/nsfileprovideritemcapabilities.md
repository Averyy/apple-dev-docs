# NSFileProviderItemCapabilities

**Framework**: File Provider  
**Kind**: struct

An item’s capabilities, which define the actions that the user can perform in the document browser.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderItemCapabilities
```

## Mentions

- [Exporting file provider metrics data](exporting-file-provider-metrics-data.md)

## Topics

### Initializers
- [init(rawValue: UInt)](nsfileprovideritemcapabilities/init(rawvalue:).md)
  Returns a newly created item capabilities value.
### Constants
- [static var allowsAddingSubItems: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsaddingsubitems.md)
  A value indicating that the user can add subitems.
- [static var allowsContentEnumerating: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowscontentenumerating.md)
  A value indicating that the item’s contents can be enumerated.
- [static var allowsDeleting: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsdeleting.md)
  A value indicating that the item can be deleted.
- [static var allowsEvicting: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsevicting.md)
  A value indicating that the system can delete the local copy of the item.
- [static var allowsReading: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsreading.md)
  A value indicating that the value can be read from.
- [static var allowsRenaming: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsrenaming.md)
  A value indicating that the item can be renamed.
- [static var allowsReparenting: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsreparenting.md)
  A value indicating that the item can be moved.
- [static var allowsTrashing: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowstrashing.md)
  A value indicating that the item can be moved to the trash.
- [static var allowsWriting: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowswriting.md)
  A value indicating that the item can be written to.
- [static var allowsExcludingFromSync: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsexcludingfromsync.md)
  A value indicating that the user can exclude the item from sync operations.
- [static var allowsAll: NSFileProviderItemCapabilities](nsfileprovideritemcapabilities/allowsall.md)
  A convenience value for enabling all capabilities.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [typealias NSFileProviderItem](nsfileprovideritem-swift.typealias.md)
  An item the File Provider extension manages.
- [protocol NSFileProviderItemProtocol](nsfileprovideritemprotocol.md)
  A protocol that defines the properties of an item managed by the File Provider extension.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [struct NSFileProviderTypeAndCreator](nsfileprovidertypeandcreator.md)
  A structure that contains the file type and file creator codes for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemcapabilities)*