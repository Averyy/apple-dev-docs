# generationIdentifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An opaque generation identifier which can be compared using `==` to determine if the data in a document has been modified.

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
var generationIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)? { get }
```

## Discussion

For URLs which refer to the same file inode, the generation identifier will change when the data in the file’s data fork is changed (changes to extended attributes or other file system metadata do not change the generation identifier). For URLs which refer to the same directory inode, the generation identifier will change when direct children of that directory are added, removed or renamed (changes to the data of the direct children of that directory will not change the generation identifier). The generation identifier is persistent across system restarts. The generation identifier is tied to a specific document on a specific volume and is not transferred when the document is copied to another volume. This property is not supported by all volumes.

## See Also

### Universal resource values
- [var addedToDirectoryDate: Date?](./addedtodirectorydate.md)
  The date the resource was created, or renamed into or within its parent directory.
- [var allValues: [URLResourceKey : Any]](./allvalues.md)
  A loosely-typed dictionary containing all keys and values.
- [var attributeModificationDate: Date?](./attributemodificationdate.md)
  The time the resource’s attributes were last modified.
- [var canonicalPath: String?](./canonicalpath.md)
  The URL’s path as a canonical absolute file system path.
- [var contentAccessDate: Date?](./contentaccessdate.md)
  The date the resource was last accessed.
- [var contentModificationDate: Date?](./contentmodificationdate.md)
  The time the resource content was last modified.
- [var creationDate: Date?](./creationdate.md)
  The date the resource was created.
- [var customIcon: NSImage?](./customicon.md)
- [var effectiveIcon: AnyObject?](./effectiveicon.md)
- [var hasHiddenExtension: Bool?](./hashiddenextension.md)
  True for resources whose filename extension is removed from the localized name property.
- [var isAliasFile: Bool?](./isaliasfile.md)
  true if the resource is a Finder alias file or a symlink, false otherwise
- [var isExcludedFromBackup: Bool?](./isexcludedfrombackup.md)
  True if resource should be excluded from backups, false otherwise.
- [var isHidden: Bool?](./ishidden.md)
  True for resources normally not displayed to users.
- [var isPackage: Bool?](./ispackage.md)
  True for packaged directories.
- [var isReadable: Bool?](./isreadable.md)
  True if this process (as determined by EUID) can read the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/generationidentifier)*