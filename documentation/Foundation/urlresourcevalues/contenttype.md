# contentType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The resource’s type.

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
var contentType: UTType? { get }
```

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
- [var isPackage: Bool?](./ispackage.md)
  True for packaged directories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresourcevalues/contenttype)*