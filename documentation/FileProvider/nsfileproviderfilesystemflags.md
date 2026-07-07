# NSFileProviderFileSystemFlags

**Framework**: File Provider  
**Kind**: struct

Flags that define an item’s on-disk properties and its appearance in the user interface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderFileSystemFlags
```

#### Overview

The flags define the on-disk properties of the item. The system modifies the item’s appearance based on these flags.

## Topics

### Flags
- [static var userReadable: NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags/userreadable.md)
  The user can read the item.
- [static var userWritable: NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags/userwritable.md)
  The user can modify the item.
- [static var userExecutable: NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags/userexecutable.md)
  The user can execute the item.
- [static var hidden: NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags/hidden.md)
  By default, the system hides the item when the user views the file system.
- [static var pathExtensionHidden: NSFileProviderFileSystemFlags](nsfileproviderfilesystemflags/pathextensionhidden.md)
  By default, the system hides the item’s extension when showing its filename.
### Initializers
- [init(rawValue: UInt)](nsfileproviderfilesystemflags/init(rawvalue:).md)
  Creates a new file system flag from the provided value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var extendedAttributes: [String : Data]](nsfileprovideritemprotocol/extendedattributes.md)
  The extended file attributes synced by the File Provider extension.
- [var fileSystemFlags: NSFileProviderFileSystemFlags](nsfileprovideritemprotocol/filesystemflags.md)
  Flags that define an item’s on-disk properties and its appearance in the user interface.
- [var tagData: Data?](nsfileprovideritemprotocol/tagdata.md)
  An abstract data blob representing the tags associated with the item.
- [var userInfo: [AnyHashable : Any]?](nsfileprovideritemprotocol/userinfo.md)
  A property list that contains additional data about the item.
- [var favoriteRank: NSNumber?](nsfileprovideritemprotocol/favoriterank.md)
  A 64-bit, unsigned integer indicating the order of the favorite item in the Favorites list.
- [let NSFileProviderFavoriteRankUnranked: UInt64](nsfileproviderfavoriterankunranked.md)
  A value that indicates that the item is not ranked.
- [var typeAndCreator: NSFileProviderTypeAndCreator](nsfileprovideritemprotocol/typeandcreator.md)
  The file type and creator codes for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderfilesystemflags)*