# documentIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A value that the kernel assigns to identify a document.

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
var documentIdentifier: Int? { get }
```

## Discussion

The kernel uses a document identifier, which can be either a file or a directory, to identify the document regardless of where it moves on a volume.

The document identifier survives safe-save operation, and is sticky to the path the kernel assigns. [`replaceItem(at:withItemAt:backupItemName:options:resultingItemURL:)`](../filemanager/replaceitem%28at,withitemat,backupitemname,options,resultingitemurl%29.md) is the preferred safe-save API. The document identifier is persistent across system restarts, and doesn’t transfer when you copy the file. Document identifiers are only unique within a single volume. Not all volumes support this property.

## See Also

### File values
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
- [var totalFileSize: Int?](./totalfilesize.md)
  The total displayable size of the file, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/documentidentifier)*