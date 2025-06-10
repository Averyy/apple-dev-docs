# FileAttributeKey

**Framework**: Foundation  
**Kind**: struct

Keys in dictionaries used to get and set file attributes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct FileAttributeKey
```

#### Discussion

These keys are used with the methods listed in the Getting and Setting Attributes topic of [`FileManager`](filemanager.md).

## Topics

### Creating a File Attribute Key
- [init(String)](fileattributekey/init(_:).md)
  Creates a file attribute key from a string.
- [init(rawValue: String)](fileattributekey/init(rawvalue:).md)
  Creates a file attribute key from a raw value string.
### Accessing File Attributes
- [static let appendOnly: FileAttributeKey](fileattributekey/appendonly.md)
  The key in a file attribute dictionary whose value indicates whether the file is read-only.
- [static let busy: FileAttributeKey](fileattributekey/busy.md)
  The key in a file attribute dictionary whose value indicates whether the file is busy.
- [static let creationDate: FileAttributeKey](fileattributekey/creationdate.md)
  The key in a file attribute dictionary whose value indicates the file’s creation date.
- [static let deviceIdentifier: FileAttributeKey](fileattributekey/deviceidentifier.md)
  The key in a file attribute dictionary whose value indicates the identifier for the device on which the file resides.
- [static let extensionHidden: FileAttributeKey](fileattributekey/extensionhidden.md)
  The key in a file attribute dictionary whose value indicates whether the file’s extension is hidden.
- [static let groupOwnerAccountID: FileAttributeKey](fileattributekey/groupowneraccountid.md)
  The key in a file attribute dictionary whose value indicates the file’s group ID.
- [static let groupOwnerAccountName: FileAttributeKey](fileattributekey/groupowneraccountname.md)
  The key in a file attribute dictionary whose value indicates the group name of the file’s owner.
- [static let hfsCreatorCode: FileAttributeKey](fileattributekey/hfscreatorcode.md)
  The key in a file attribute dictionary whose value indicates the file’s HFS creator code.
- [static let hfsTypeCode: FileAttributeKey](fileattributekey/hfstypecode.md)
  The key in a file attribute dictionary whose value indicates the file’s HFS type code.
- [static let immutable: FileAttributeKey](fileattributekey/immutable.md)
  The key in a file attribute dictionary whose value indicates whether the file is mutable.
- [static let modificationDate: FileAttributeKey](fileattributekey/modificationdate.md)
  The key in a file attribute dictionary whose value indicates the file’s last modified date.
- [static let ownerAccountID: FileAttributeKey](fileattributekey/owneraccountid.md)
  The key in a file attribute dictionary whose value indicates the file’s owner’s account ID.
- [static let ownerAccountName: FileAttributeKey](fileattributekey/owneraccountname.md)
  The key in a file attribute dictionary whose value indicates the name of the file’s owner.
- [static let posixPermissions: FileAttributeKey](fileattributekey/posixpermissions.md)
  The key in a file attribute dictionary whose value indicates the file’s Posix permissions.
- [static let protectionKey: FileAttributeKey](fileattributekey/protectionkey.md)
  The key in a file attribute dictionary whose value identifies the protection level for this file.
- [static let referenceCount: FileAttributeKey](fileattributekey/referencecount.md)
  The key in a file attribute dictionary whose value indicates the file’s reference count.
- [static let size: FileAttributeKey](fileattributekey/size.md)
  The key in a file attribute dictionary whose value indicates the file’s size in bytes.
- [static let systemFileNumber: FileAttributeKey](fileattributekey/systemfilenumber.md)
  The key in a file attribute dictionary whose value indicates the file’s filesystem file number.
- [static let systemFreeNodes: FileAttributeKey](fileattributekey/systemfreenodes.md)
  The key in a file system attribute dictionary whose value indicates the number of free nodes in the file system.
- [static let systemFreeSize: FileAttributeKey](fileattributekey/systemfreesize.md)
  The key in a file system attribute dictionary whose value indicates the amount of free space on the file system.
- [static let systemNodes: FileAttributeKey](fileattributekey/systemnodes.md)
  The key in a file system attribute dictionary whose value indicates the number of nodes in the file system.
- [static let systemNumber: FileAttributeKey](fileattributekey/systemnumber.md)
  The key in a file system attribute dictionary whose value indicates the filesystem number of the file system.
- [static let systemSize: FileAttributeKey](fileattributekey/systemsize.md)
  The key in a file system attribute dictionary whose value indicates the size of the file system.
- [static let type: FileAttributeKey](fileattributekey/type.md)
  The key in a file attribute dictionary whose value indicates the file’s type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FileManager.DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md)
  Options for enumerating the contents of directories.
- [FileManager.SearchPathDirectory](filemanager/searchpathdirectory.md)
  The location of significant directories.
- [FileManager.SearchPathDomainMask](filemanager/searchpathdomainmask.md)
  Domain constants specifying base locations to use when you search for significant directories.
- [struct FileAttributeType](fileattributetype.md)
  Values representing a file’s type attribute.
- [struct FileProtectionType](fileprotectiontype.md)
  Protection level values that can be associated with a file attribute key.
- [struct URLFileProtection](urlfileprotection.md)
  Protection-level values for a URL resource key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileattributekey)*