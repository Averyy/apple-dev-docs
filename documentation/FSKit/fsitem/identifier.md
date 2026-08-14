# FSItem.Identifier

**Framework**: FSKit  
**Kind**: enum

The unique identifier for an item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum Identifier
```

#### Overview

Use this type when packing items for an enumeration in [`packEntry(name:itemType:itemID:nextCookie:attributes:)`](fsdirectoryentrypacker/packentry(name:itemtype:itemid:nextcookie:attributes:).md). Either provide a unique identifier like an inode number, or one of the special enumeration cases this type defines, like [`FSItem.Identifier.rootDirectory`](fsitem/identifier/rootdirectory.md).

## Topics

### Working with special identifiers
- [FSItem.Identifier.invalid](fsitem/identifier/invalid.md)
  The identifier for an invalid item.
- [FSItem.Identifier.parentOfRoot](fsitem/identifier/parentofroot.md)
  The identifier for an item that serves as the parent of the root directory.
- [FSItem.Identifier.rootDirectory](fsitem/identifier/rootdirectory.md)
  The item identifier for the root directory.
### Working with raw values
- [init?(rawValue: UInt64)](fsitem/identifier/init(rawvalue:).md)
### Initializers
- [init(UInt64)](fsitem/identifier/init(_:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [FSItem.ItemType](fsitem/itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/identifier)*