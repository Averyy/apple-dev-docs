# FSFreeSpace

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

A free space object that pairs free space values with atomic sequence numbers.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSFreeSpace
```

```objc
@interface FSFreeSpace : NSObject
```

## Topics

### Creating a free space instance
- [init()](./fsfreespace/init%28%29.md)
  Creates an unpopulated free space instance.
### Setting the free space value
- [func populate(bytes: UInt64)](./fsfreespace/populate%28bytes%29.md)
  Populates this instance with the given free space value and atomically assigns a sequence number.
### Working with special instances
- [class var noUpdate: FSFreeSpace](./fsfreespace/noupdate.md)
  A sentinel instance that indicates no free space update occurred.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating a create-item result
- [init?(newItem: FSItem, newItemName: FSFileName, newItemAttributes: FSItem.Attributes, directoryAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)](./fscreateitemresult/init%28newitem,newitemname,newitemattributes,directoryattributes,freespace%29.md)
  Creates a result for an item-creation operation.
- [class FSFileName](./fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](./fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfreespace)*