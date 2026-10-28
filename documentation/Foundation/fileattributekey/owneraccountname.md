# ownerAccountName

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The key in a file attribute dictionary whose value indicates the name of the file’s owner.

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
static let ownerAccountName: FileAttributeKey
```

```c
extern NSFileAttributeKey const NSFileOwnerAccountName;
```

## Discussion

The corresponding value is an [`NSString`](../nsstring.md) object.

## See Also

### Accessing File Attributes
- [static let appendOnly: FileAttributeKey](./appendonly.md)
  The key in a file attribute dictionary whose value indicates whether the file is read-only.
- [static let busy: FileAttributeKey](./busy.md)
  The key in a file attribute dictionary whose value indicates whether the file is busy.
- [static let creationDate: FileAttributeKey](./creationdate.md)
  The key in a file attribute dictionary whose value indicates the file’s creation date.
- [static let deviceIdentifier: FileAttributeKey](./deviceidentifier.md)
  The key in a file attribute dictionary whose value indicates the identifier for the device on which the file resides.
- [static let extensionHidden: FileAttributeKey](./extensionhidden.md)
  The key in a file attribute dictionary whose value indicates whether the file’s extension is hidden.
- [static let groupOwnerAccountID: FileAttributeKey](./groupowneraccountid.md)
  The key in a file attribute dictionary whose value indicates the file’s group ID.
- [static let groupOwnerAccountName: FileAttributeKey](./groupowneraccountname.md)
  The key in a file attribute dictionary whose value indicates the group name of the file’s owner.
- [static let hfsCreatorCode: FileAttributeKey](./hfscreatorcode.md)
  The key in a file attribute dictionary whose value indicates the file’s HFS creator code.
- [static let hfsTypeCode: FileAttributeKey](./hfstypecode.md)
  The key in a file attribute dictionary whose value indicates the file’s HFS type code.
- [static let immutable: FileAttributeKey](./immutable.md)
  The key in a file attribute dictionary whose value indicates whether the file is mutable.
- [static let modificationDate: FileAttributeKey](./modificationdate.md)
  The key in a file attribute dictionary whose value indicates the file’s last modified date.
- [static let ownerAccountID: FileAttributeKey](./owneraccountid.md)
  The key in a file attribute dictionary whose value indicates the file’s owner’s account ID.
- [static let posixPermissions: FileAttributeKey](./posixpermissions.md)
  The key in a file attribute dictionary whose value indicates the file’s Posix permissions.
- [static let protectionKey: FileAttributeKey](./protectionkey.md)
  The key in a file attribute dictionary whose value identifies the protection level for this file.
- [static let referenceCount: FileAttributeKey](./referencecount.md)
  The key in a file attribute dictionary whose value indicates the file’s reference count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileattributekey/owneraccountname)*