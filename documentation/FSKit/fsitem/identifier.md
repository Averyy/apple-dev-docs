# FSItem.Identifier

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

The unique identifier for an item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum Identifier
```

```c
enum FSItemID : UInt64;
```

## Overview

Use this type when packing items for an enumeration in [`packEntry(name:itemType:itemID:nextCookie:attributes:)`](../fsdirectoryentrypacker/packentry%28name,itemtype,itemid,nextcookie,attributes%29.md). Either provide a unique identifier like an inode number, or one of the special enumeration cases this type defines, like [`FSItem.Identifier.rootDirectory`](./identifier/rootdirectory.md).

## Topics

### Working with special identifiers
- [FSItem.Identifier.invalid](./identifier/invalid.md)
  The identifier for an invalid item.
- [FSItem.Identifier.parentOfRoot](./identifier/parentofroot.md)
  The identifier for an item that serves as the parent of the root directory.
- [FSItem.Identifier.rootDirectory](./identifier/rootdirectory.md)
  The item identifier for the root directory.
### Working with raw values
- [init?(rawValue: UInt64)](./identifier/init%28rawvalue%29.md)
### Initializers
- [init(UInt64)](./identifier/init%28_%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Identifying an item
- [FSItem.ItemType](./itemtype.md)
  An enumeration of item types, such as file, directory, or symbolic link.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/identifier)*