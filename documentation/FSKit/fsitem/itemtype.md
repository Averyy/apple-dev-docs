# FSItem.ItemType

**Framework**: FSKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration of item types, such as file, directory, or symbolic link.

**Availability**:
- macOS 15.4+

## Declaration

```swift
enum ItemType
```

```c
enum FSItemType : NSInteger;
```

## Topics

### Working with item types
- [FSItem.ItemType.file](./itemtype/file.md)
  The item type of a regular file.
- [FSItem.ItemType.directory](./itemtype/directory.md)
  The item type of a directory.
- [FSItem.ItemType.symlink](./itemtype/symlink.md)
  The item type of a symbolic link.
- [FSItem.ItemType.fifo](./itemtype/fifo.md)
  The item type of a first-in/first-out named pipe.
- [FSItem.ItemType.charDevice](./itemtype/chardevice.md)
  The item type of a character device.
- [FSItem.ItemType.blockDevice](./itemtype/blockdevice.md)
  The item type of a block device.
- [FSItem.ItemType.socket](./itemtype/socket.md)
  The item type of a socket.
- [FSItem.ItemType.unknown](./itemtype/unknown.md)
  The item type of an unknown item.
### Working with raw values
- [init?(rawValue: Int)](./itemtype/init%28rawvalue%29.md)

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
- [FSItem.Identifier](./identifier.md)
  The unique identifier for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/itemtype)*