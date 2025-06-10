# systemSize

**Framework**: Foundation  
**Kind**: property

The key in a file system attribute dictionary whose value indicates the size of the file system.

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
static let systemSize: FileAttributeKey
```

#### Discussion

The corresponding value is an [`NSNumber`](nsnumber.md) object that specifies the size of the file system in bytes. The value is determined by `statfs()`.

> ❗ **Important**:  This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [`Describing use of required reason API`](https://developer.apple.com/documentation/BundleResources/describing-use-of-required-reason-api).

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
- [static let protectionKey: FileAttributeKey](fileattributekey/protectionkey.md)
  The key in a file attribute dictionary whose value identifies the protection level for this file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/fileattributekey/systemsize)*