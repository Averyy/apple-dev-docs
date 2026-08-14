# FSFreeSpace

**Framework**: FSKit  
**Kind**: class

A free space object that pairs free space values with atomic sequence numbers.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSFreeSpace
```

## Topics

### Creating a free space instance
- [init()](fsfreespace/init.md)
  Creates an unpopulated free space instance.
### Setting the free space value
- [func populate(bytes: UInt64)](fsfreespace/populate(bytes:).md)
  Populates this instance with the given free space value and atomically assigns a sequence number.
### Working with special instances
- [class var noUpdate: FSFreeSpace](fsfreespace/noupdate.md)
  A sentinel instance that indicates no free space update occurred.

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

- [init?(newItem: FSItem, newItemName: FSFileName, newItemAttributes: FSItem.Attributes, directoryAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](fscreateitemresult/init(newitem:newitemname:newitemattributes:directoryattributes:freespace:).md)
  Creates a result for an item-creation operation.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfreespace)*