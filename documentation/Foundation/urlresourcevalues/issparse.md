# isSparse

**Framework**: Foundation  
**Kind**: property

A Boolean value that indicates whether the file has sparse regions.

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
var isSparse: Bool? { get }
```

## See Also

- [var documentIdentifier: Int?](urlresourcevalues/documentidentifier.md)
  A value that the kernel assigns to identify a document.
- [var fileContentIdentifier: Int64?](urlresourcevalues/filecontentidentifier.md)
  A value APFS assigns that identifies a file’s content data stream.
- [var fileAllocatedSize: Int?](urlresourcevalues/fileallocatedsize.md)
  The total allocated size on-disk for the file, in bytes.
- [var fileProtection: URLFileProtection?](urlresourcevalues/fileprotection.md)
  The protection level for the file.
- [var fileResourceIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)?](urlresourcevalues/fileresourceidentifier.md)
  An identifier for comparing two file system objects for equality.
- [var fileResourceType: URLFileResourceType?](urlresourcevalues/fileresourcetype.md)
  The type of the file system object.
- [var fileSecurity: NSFileSecurity?](urlresourcevalues/filesecurity.md)
  The file system object’s security information.
- [var fileSize: Int?](urlresourcevalues/filesize.md)
  The total file size, in bytes.
- [var isPurgeable: Bool?](urlresourcevalues/ispurgeable.md)
  A Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [var mayHaveExtendedAttributes: Bool?](urlresourcevalues/mayhaveextendedattributes.md)
  A Boolean value that indicates the file may have extended attributes.
- [var isExecutable: Bool?](urlresourcevalues/isexecutable.md)
  A Boolean value that indicates whether you can execute the file resource or search a directory resource.
- [var isRegularFile: Bool?](urlresourcevalues/isregularfile.md)
  A Boolean value that indicates whether the resource is a regular file.
- [var mayShareFileContent: Bool?](urlresourcevalues/maysharefilecontent.md)
  A Boolean value that indicates whether the cloned files and their original files may share data blocks.
- [var totalFileAllocatedSize: Int?](urlresourcevalues/totalfileallocatedsize.md)
  The total allocated size of the file, in bytes.
- [var totalFileSize: Int?](urlresourcevalues/totalfilesize.md)
  The total displayable size of the file, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/issparse)*