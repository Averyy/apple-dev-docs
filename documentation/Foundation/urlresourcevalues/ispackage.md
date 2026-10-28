# isPackage

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

True for packaged directories.

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
var isPackage: Bool? { get set }
```

## Discussion

> **Note**:  You can only set or clear this property on directories; if you try to set this property on non-directory objects, the property is ignored. If the directory is a package for some other reason (extension type, etc), setting this property to false will have no effect.

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
- [var generationIdentifier: (any NSCopying & NSSecureCoding & NSObjectProtocol)?](./generationidentifier.md)
  An opaque generation identifier which can be compared using `==` to determine if the data in a document has been modified.
- [var hasHiddenExtension: Bool?](./hashiddenextension.md)
  True for resources whose filename extension is removed from the localized name property.
- [var isAliasFile: Bool?](./isaliasfile.md)
  true if the resource is a Finder alias file or a symlink, false otherwise
- [var isExcludedFromBackup: Bool?](./isexcludedfrombackup.md)
  True if resource should be excluded from backups, false otherwise.
- [var isHidden: Bool?](./ishidden.md)
  True for resources normally not displayed to users.
- [var isReadable: Bool?](./isreadable.md)
  True if this process (as determined by EUID) can read the resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/ispackage)*