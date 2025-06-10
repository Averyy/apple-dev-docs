# protectionKey

**Framework**: Foundation  
**Kind**: property

The key in a file attribute dictionary whose value identifies the protection level for this file.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let protectionKey: FileAttributeKey
```

#### Discussion

The corresponding value is an [`NSString`](nsstring.md) value. For a list of possible values, see `File Protection Values`.

## See Also

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
- [static let referenceCount: FileAttributeKey](fileattributekey/referencecount.md)
  The key in a file attribute dictionary whose value indicates the file’s reference count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileattributekey/protectionkey)*