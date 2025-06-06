# fileSizeKey

**Framework**: Foundation  
**Kind**: property

The key for the file’s size, in bytes.

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
static let fileSizeKey: URLResourceKey
```

#### Discussion

The system returns the read-only value as an [`NSNumber`](nsnumber.md) object.

## See Also

- [static let fileAllocatedSizeKey: URLResourceKey](urlresourcekey/fileallocatedsizekey.md)
  The key for the total allocated size on-disk for the file.
- [static let fileProtectionKey: URLResourceKey](urlresourcekey/fileprotectionkey.md)
  The key for the protection level of the file.
- [struct URLFileProtection](urlfileprotection.md)
  Protection-level values for a URL resource key.
- [static let fileContentIdentifierKey: URLResourceKey](urlresourcekey/filecontentidentifierkey.md)
  The key for a value that APFS assigns to identify a file’s content data stream.
- [static let fileResourceIdentifierKey: URLResourceKey](urlresourcekey/fileresourceidentifierkey.md)
  The key for the resource’s unique identifier.
- [static let fileResourceTypeKey: URLResourceKey](urlresourcekey/fileresourcetypekey.md)
  The key for the resource’s object type.
- [struct URLFileResourceType](urlfileresourcetype.md)
  Possible values for the type of file resource.
- [static let fileSecurityKey: URLResourceKey](urlresourcekey/filesecuritykey.md)
  The key for the resource’s security information.
- [static let isAliasFileKey: URLResourceKey](urlresourcekey/isaliasfilekey.md)
  The key for determining whether the file is an alias.
- [static let isPackageKey: URLResourceKey](urlresourcekey/ispackagekey.md)
  The key for determining whether the resource is a file package.
- [static let isRegularFileKey: URLResourceKey](urlresourcekey/isregularfilekey.md)
  The key for determining whether the resource is a regular file rather than a directory or a symbolic link.
- [static let isPurgeableKey: URLResourceKey](urlresourcekey/ispurgeablekey.md)
  The key for a Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [static let isSparseKey: URLResourceKey](urlresourcekey/issparsekey.md)
  The key for a Boolean value that indicates whether the file has sparse regions.
- [static let mayHaveExtendedAttributesKey: URLResourceKey](urlresourcekey/mayhaveextendedattributeskey.md)
  The key for a Boolean value that indicates whether the file has extended attributes.
- [static let mayShareFileContentKey: URLResourceKey](urlresourcekey/maysharefilecontentkey.md)
  The key for a Boolean value that indicates whether cloned files and their original files may share data blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/filesizekey)*