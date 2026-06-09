# init(newItem:newItemName:newItemAttributes:directoryAttributes:freeSpace:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an item-creation operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(newItem: FSItem, newItemName: FSFileName, newItemAttributes: FSItem.Attributes, directoryAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `newItem`: The newly-created [`FSItem`](fsitem.md).
- `newItemName`: The name of the newly-created item as it exists within the file system.
- `newItemAttributes`: The [`FSItem.Attributes`](fsitem/attributes.md) of the newly-created item.
- `directoryAttributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the parent directory.
- `freeSpace`: An [`FSFreeSpace`](fsfreespace.md) instance populated with the volume’s updated free space. Passing a `nil` free space causes FSKit to calculate the free space when the operation completes, based on the volume’s [`volumeStatistics`](fsvolume/handler/volumestatistics.md) property. This behavior may lead to degraded performance.

## See Also

- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreateitemresult/init(newitem:newitemname:newitemattributes:directoryattributes:freespace:))*