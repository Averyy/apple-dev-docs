# FSDirectoryEntryPacker

**Framework**: FSKit  
**Kind**: class

An object used to provide items during a directory enumeration.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSDirectoryEntryPacker
```

#### Overview

You use this type in your implementation of [`enumerateDirectory(_:startingAt:verifier:attributes:packer:context:replyHandler:)`](fsvolume/handler/enumeratedirectory(_:startingat:verifier:attributes:packer:context:replyhandler:).md).

Packing allows your implementation to provide information FSKit needs, including each item’s name, type, and identifier (such as an inode number). Some directory enumerations require other attributes, as indicated by the [`FSItem.GetAttributesRequest`](fsitem/getattributesrequest.md) sent to the enumerate method.

## Topics

### Packing entries
- [func packEntry(name: FSFileName, itemType: FSItem.ItemType, itemID: FSItem.Identifier, nextCookie: FSDirectoryCookie, attributes: FSItem.Attributes?) -> Bool](fsdirectoryentrypacker/packentry(name:itemtype:itemid:nextcookie:attributes:).md)
  Provides a directory entry during enumeration.
- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.
- [FSItem.Identifier](fsitem/identifier.md)
  The unique identifier for an item.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [func enumerateDirectory(FSItem, startingAt: FSDirectoryCookie, verifier: FSDirectoryVerifier, attributes: FSItem.GetAttributesRequest?, packer: FSDirectoryEntryPacker, context: FSContext, replyHandler: (FSEnumerateDirectoryResult?, (any Error)?) -> Void)](fsvolume/handler/enumeratedirectory(_:startingat:verifier:attributes:packer:context:replyhandler:).md)
  Enumerates the contents of the given directory.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryCookie](fsdirectorycookie.md)
  A value that indicates a location in a directory from which to enumerate.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [struct FSDirectoryVerifier](fsdirectoryverifier.md)
  A tool to detect whether the directory contents changed since the last call to enumerate a directory.
- [class FSEnumerateDirectoryResult](fsenumeratedirectoryresult.md)
  The result of an enumerate-directory call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsdirectoryentrypacker)*