# NSFileProviderItemProtocol

**Framework**: File Provider  
**Kind**: protocol

A protocol that defines the properties of an item managed by the File Provider extension.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderItemProtocol : NSObjectProtocol
```

## Mentions

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)

#### Overview

Most of these properties are optional. A File Provider extension doesn’t need to implement all properties for all items.

## Topics

### Providing Required Properties
- [var itemIdentifier: NSFileProviderItemIdentifier](nsfileprovideritemprotocol/itemidentifier.md)
  The item’s persistent identifier.
- [var filename: String](nsfileprovideritemprotocol/filename.md)
  The item’s filename.
- [var typeIdentifier: String](nsfileprovideritemprotocol/typeidentifier.md)
  The item’s Uniform Type Identifier (UTI).
- [var contentType: UTType](nsfileprovideritemprotocol/contenttype.md)
  The item’s Uniform Type Identifier (UTI).
- [var capabilities: NSFileProviderItemCapabilities](nsfileprovideritemprotocol/capabilities.md)
  The item’s capabilities.
### Managing Content
- [var childItemCount: NSNumber?](nsfileprovideritemprotocol/childitemcount.md)
  The number of items contained by this item.
- [var documentSize: NSNumber?](nsfileprovideritemprotocol/documentsize.md)
  The document’s size, in bytes.
- [var contentPolicy: NSFileProviderContentPolicy](nsfileprovideritemprotocol/contentpolicy.md)
- [enum NSFileProviderContentPolicy](nsfileprovidercontentpolicy.md)
### Specifying Content Location
- [var parentItemIdentifier: NSFileProviderItemIdentifier](nsfileprovideritemprotocol/parentitemidentifier.md)
  The persistent identifier of the item’s parent folder.
- [var isTrashed: Bool](nsfileprovideritemprotocol/istrashed.md)
  A Boolean value that indicates whether an item is in the trash.
- [var symlinkTargetPath: String?](nsfileprovideritemprotocol/symlinktargetpath.md)
  The target of the symlink.
### Tracking Usage
- [var contentModificationDate: Date?](nsfileprovideritemprotocol/contentmodificationdate.md)
  The date the item was last modified.
- [var creationDate: Date?](nsfileprovideritemprotocol/creationdate.md)
  The date the item was created.
- [var lastUsedDate: Date?](nsfileprovideritemprotocol/lastuseddate.md)
  The date the item was last used.
### Tracking Versions
- [var itemVersion: NSFileProviderItemVersion](nsfileprovideritemprotocol/itemversion.md)
  A version object that tracks changes to an item.
- [var versionIdentifier: Data?](nsfileprovideritemprotocol/versionidentifier.md)
  A data value used to determine when the item changes.
- [var isMostRecentVersionDownloaded: Bool](nsfileprovideritemprotocol/ismostrecentversiondownloaded.md)
  A Boolean value that indicates whether the item is the most recent version downloaded from the server.
### Monitoring File Transfers
- [var isUploading: Bool](nsfileprovideritemprotocol/isuploading.md)
  A Boolean value that indicates whether the item is currently uploading to your remote server.
- [var isUploaded: Bool](nsfileprovideritemprotocol/isuploaded.md)
  A Boolean value that indicates whether the item has been uploaded to your remote server.
- [var uploadingError: (any Error)?](nsfileprovideritemprotocol/uploadingerror.md)
  An object describing an error that occurred while uploading the item.
- [var isDownloading: Bool](nsfileprovideritemprotocol/isdownloading.md)
  A Boolean value that indicates whether the item is currently downloading from your remote server.
- [var isDownloaded: Bool](nsfileprovideritemprotocol/isdownloaded.md)
  A Boolean value that indicates whether the item has been downloaded from your remote server.
- [var downloadingError: (any Error)?](nsfileprovideritemprotocol/downloadingerror.md)
  An object describing an error that occurred while downloading the item.
### Sharing
- [var isShared: Bool](nsfileprovideritemprotocol/isshared.md)
  A Boolean value that indicates whether the item is shared with other users.
- [var isSharedByCurrentUser: Bool](nsfileprovideritemprotocol/issharedbycurrentuser.md)
  A Boolean value that indicates whether the item was shared by the current user.
- [var mostRecentEditorNameComponents: PersonNameComponents?](nsfileprovideritemprotocol/mostrecenteditornamecomponents.md)
  The most recent editor’s name.
- [var ownerNameComponents: PersonNameComponents?](nsfileprovideritemprotocol/ownernamecomponents.md)
  The name of the item’s owner.
### Managing Metadata
- [var extendedAttributes: [String : Data]](nsfileprovideritemprotocol/extendedattributes.md)
  The extended file attributes synced by the File Provider extension.
- [var fileSystemFlags: NSFileProviderFileSystemFlags](nsfileprovideritemprotocol/filesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [struct NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [var tagData: Data?](nsfileprovideritemprotocol/tagdata.md)
  An abstract data blob representing the tags associated with the item.
- [var userInfo: [AnyHashable : Any]?](nsfileprovideritemprotocol/userinfo.md)
  A property list that contains additional data about the item.
- [var favoriteRank: NSNumber?](nsfileprovideritemprotocol/favoriterank.md)
  A 64-bit, unsigned integer indicating the order of the favorite item in the Favorites list.
- [let NSFileProviderFavoriteRankUnranked: UInt64](nsfileproviderfavoriterankunranked.md)
  A value that indicates that the item is not ranked.
- [var typeAndCreator: NSFileProviderTypeAndCreator](nsfileprovideritemprotocol/typeandcreator.md)
  The file type and creator codes for the item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSFileProviderItemDecorating](nsfileprovideritemdecorating.md)

## See Also

- [typealias NSFileProviderItem](nsfileprovideritem-swift.typealias.md)
  An item the File Provider extension manages.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [struct NSFileProviderItemCapabilities](nsfileprovideritemcapabilities.md)
  An item’s capabilities, which define the actions that the user can perform in the document browser.
- [struct NSFileProviderTypeAndCreator](nsfileprovidertypeandcreator.md)
  A structure that contains the file type and file creator codes for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol)*