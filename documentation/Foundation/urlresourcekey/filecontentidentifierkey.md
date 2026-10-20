# fileContentIdentifierKey

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The key for a value that APFS assigns to identify a file’s content data stream.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
static let fileContentIdentifierKey: URLResourceKey
```

```c
extern NSURLResourceKey const NSURLFileContentIdentifierKey;
```

#### Discussion

APFS allows only cloned files and their originals to have the same identifier.

## See Also

### File keys
- [static let fileAllocatedSizeKey: URLResourceKey](./fileallocatedsizekey.md)
  The key for the total allocated size on-disk for the file.
- [static let fileProtectionKey: URLResourceKey](./fileprotectionkey.md)
  The key for the protection level of the file.
- [struct URLFileProtection](../urlfileprotection.md)
  Protection-level values for a URL resource key.
- [static let fileResourceIdentifierKey: URLResourceKey](./fileresourceidentifierkey.md)
  The key for the resource’s unique identifier.
- [static let fileResourceTypeKey: URLResourceKey](./fileresourcetypekey.md)
  The key for the resource’s object type.
- [struct URLFileResourceType](../urlfileresourcetype.md)
  Possible values for the type of file resource.
- [static let fileSecurityKey: URLResourceKey](./filesecuritykey.md)
  The key for the resource’s security information.
- [static let fileSizeKey: URLResourceKey](./filesizekey.md)
  The key for the file’s size, in bytes.
- [static let isAliasFileKey: URLResourceKey](./isaliasfilekey.md)
  The key for determining whether the file is an alias.
- [static let isPackageKey: URLResourceKey](./ispackagekey.md)
  The key for determining whether the resource is a file package.
- [static let isRegularFileKey: URLResourceKey](./isregularfilekey.md)
  The key for determining whether the resource is a regular file rather than a directory or a symbolic link.
- [static let isPurgeableKey: URLResourceKey](./ispurgeablekey.md)
  The key for a Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [static let isSparseKey: URLResourceKey](./issparsekey.md)
  The key for a Boolean value that indicates whether the file has sparse regions.
- [static let mayHaveExtendedAttributesKey: URLResourceKey](./mayhaveextendedattributeskey.md)
  The key for a Boolean value that indicates whether the file has extended attributes.
- [static let mayShareFileContentKey: URLResourceKey](./maysharefilecontentkey.md)
  The key for a Boolean value that indicates whether cloned files and their original files may share data blocks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcekey/filecontentidentifierkey)*