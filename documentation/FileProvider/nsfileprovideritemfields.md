# NSFileProviderItemFields

**Framework**: File Provider  
**Kind**: struct

Fields that specify which of the item’s properties have changed.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderItemFields
```

#### Overview

Most of the fields correspond to properties in the [`NSFileProviderItemProtocol`](nsfileprovideritemprotocol.md) protocol.

## Topics

### Specifying the Required Fields
- [static var filename: NSFileProviderItemFields](nsfileprovideritemfields/filename.md)
  The item’s filename.
- [static var contents: NSFileProviderItemFields](nsfileprovideritemfields/contents.md)
  The item’s content.
### Specifying Content Location
- [static var parentItemIdentifier: NSFileProviderItemFields](nsfileprovideritemfields/parentitemidentifier.md)
  The identity of the directory that contains the item.
### Tracking Usage
- [static var contentModificationDate: NSFileProviderItemFields](nsfileprovideritemfields/contentmodificationdate.md)
  The item’s modification date.
- [static var creationDate: NSFileProviderItemFields](nsfileprovideritemfields/creationdate.md)
  The item’s creation date.
- [static var lastUsedDate: NSFileProviderItemFields](nsfileprovideritemfields/lastuseddate.md)
  The date the item was last used.
### Working with Metadata
- [static var extendedAttributes: NSFileProviderItemFields](nsfileprovideritemfields/extendedattributes.md)
  The item’s extended attributes.
- [static var fileSystemFlags: NSFileProviderItemFields](nsfileprovideritemfields/filesystemflags.md)
  The flags describing the item’s on-disk representation.
- [static var tagData: NSFileProviderItemFields](nsfileprovideritemfields/tagdata.md)
  The tags for the item.
- [static var favoriteRank: NSFileProviderItemFields](nsfileprovideritemfields/favoriterank.md)
  The item’s favorite rank.
- [static var typeAndCreator: NSFileProviderItemFields](nsfileprovideritemfields/typeandcreator.md)
  The file type and creator codes for the item.
### Initializers
- [init(rawValue: UInt)](nsfileprovideritemfields/init(rawvalue:).md)
  Creates an option instance from the raw value.

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

- [class NSFileProviderItemVersion](nsfileprovideritemversion.md)
  The version of the item’s content and its metadata.
- [class NSFileProviderRequest](nsfileproviderrequest.md)
  An object that provides information about the application requesting data from the File Provider extension.
- [protocol NSFileProviderItemDecorating](nsfileprovideritemdecorating.md)
  Support for decorating items.
- [struct NSFileProviderItemDecorationIdentifier](nsfileprovideritemdecorationidentifier.md)
  A decoration identifier defined in the File Provider extension’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemfields)*