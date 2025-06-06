# URLFileResourceType

**Framework**: Foundation  
**Kind**: struct

Possible values for the type of file resource.

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
struct URLFileResourceType
```

## Topics

### Creating a File Resource Type Instance
- [init(rawValue: String)](urlfileresourcetype/init(rawvalue:).md)
  Creates a file resource type from the provided constant string.
### Constants
- [static let namedPipe: URLFileResourceType](urlfileresourcetype/namedpipe.md)
  The resource is a named pipe.
- [static let characterSpecial: URLFileResourceType](urlfileresourcetype/characterspecial.md)
  The resource is a character special file.
- [static let directory: URLFileResourceType](urlfileresourcetype/directory.md)
  The resource is a directory.
- [static let blockSpecial: URLFileResourceType](urlfileresourcetype/blockspecial.md)
  The resource is a block special file.
- [static let regular: URLFileResourceType](urlfileresourcetype/regular.md)
  The resource is a regular file.
- [static let symbolicLink: URLFileResourceType](urlfileresourcetype/symboliclink.md)
  The resource is a symbolic link.
- [static let socket: URLFileResourceType](urlfileresourcetype/socket.md)
  The resource is a socket.
- [static let unknown: URLFileResourceType](urlfileresourcetype/unknown.md)
  The resource’s type is unknown.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [static let fileSecurityKey: URLResourceKey](urlresourcekey/filesecuritykey.md)
  The key for the resource’s security information.
- [static let fileSizeKey: URLResourceKey](urlresourcekey/filesizekey.md)
  The key for the file’s size, in bytes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlfileresourcetype)*