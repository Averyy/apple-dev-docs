# totalFileSize

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The total displayable size of the file, in bytes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var totalFileSize: Int? { get }
```

## Discussion

The allocated size in bytes may include space used by metadata. The property returns `nil` if the information isn’t available.

> **Note**:  Only applicable to regular files.

## See Also

### File values
- [var documentIdentifier: Int?](./documentidentifier.md)
  A value that the kernel assigns to identify a document.
- [var fileContentIdentifier: Int64?](./filecontentidentifier.md)
  A value APFS assigns that identifies a file’s content data stream.
- [var fileAllocatedSize: Int?](./fileallocatedsize.md)
  The total allocated size on-disk for the file, in bytes.
- [var fileProtection: URLFileProtection?](./fileprotection.md)
  The protection level for the file.
- [var fileResourceIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)?](./fileresourceidentifier.md)
  An identifier for comparing two file system objects for equality.
- [var fileResourceType: URLFileResourceType?](./fileresourcetype.md)
  The type of the file system object.
- [var fileSecurity: NSFileSecurity?](./filesecurity.md)
  The file system object’s security information.
- [var fileSize: Int?](./filesize.md)
  The total file size, in bytes.
- [var isPurgeable: Bool?](./ispurgeable.md)
  A Boolean value that indicates whether the file system can delete a file when the system needs to free space.
- [var isSparse: Bool?](./issparse.md)
  A Boolean value that indicates whether the file has sparse regions.
- [var mayHaveExtendedAttributes: Bool?](./mayhaveextendedattributes.md)
  A Boolean value that indicates the file may have extended attributes.
- [var isExecutable: Bool?](./isexecutable.md)
  A Boolean value that indicates whether you can execute the file resource or search a directory resource.
- [var isRegularFile: Bool?](./isregularfile.md)
  A Boolean value that indicates whether the resource is a regular file.
- [var mayShareFileContent: Bool?](./maysharefilecontent.md)
  A Boolean value that indicates whether the cloned files and their original files may share data blocks.
- [var totalFileAllocatedSize: Int?](./totalfileallocatedsize.md)
  The total allocated size of the file, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/totalfilesize)*