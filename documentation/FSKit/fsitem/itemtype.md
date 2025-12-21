# FSItem.ItemType

**Framework**: FSKit  
**Kind**: enum

An enumeration of item types, such as file, directory, or symbolic link.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum ItemType
```

## Topics

### Working with item types
- [FSItem.ItemType.file](fsitem/itemtype/file.md)
  The item type of a regular file.
- [FSItem.ItemType.directory](fsitem/itemtype/directory.md)
  The item type of a directory.
- [FSItem.ItemType.symlink](fsitem/itemtype/symlink.md)
  The item type of a symbolic link.
- [FSItem.ItemType.fifo](fsitem/itemtype/fifo.md)
  The item type of a first-in/first-out named pipe.
- [FSItem.ItemType.charDevice](fsitem/itemtype/chardevice.md)
  The item type of a character device.
- [FSItem.ItemType.blockDevice](fsitem/itemtype/blockdevice.md)
  The item type of a block device.
- [FSItem.ItemType.socket](fsitem/itemtype/socket.md)
  The item type of a socket.
- [FSItem.ItemType.unknown](fsitem/itemtype/unknown.md)
  The item type of an unknown item.
### Working with raw values
- [init?(rawValue: Int)](fsitem/itemtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [FSItem.Identifier](fsitem/identifier.md)
  The unique identifier for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/itemtype)*