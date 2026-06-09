# init(newName:renamedItemAttributes:sourceDirectoryAttributes:destinationDirectoryAttributes:overItemAttributes:freeSpace:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an item-renaming operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(newName: FSFileName, renamedItemAttributes: FSItem.Attributes, sourceDirectoryAttributes: FSItem.Attributes, destinationDirectoryAttributes: FSItem.Attributes, overItemAttributes: FSItem.Attributes?, freeSpace: FSFreeSpace?)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `newName`: The updated item name as it exists within the destination directory.
- `renamedItemAttributes`: The [`FSItem.Attributes`](fsitem/attributes.md) of the renamed item.
- `sourceDirectoryAttributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the source directory.
- `destinationDirectoryAttributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the destination directory.
- `overItemAttributes`: The [`FSItem.Attributes`](fsitem/attributes.md) of the overwritten item, if any. Pass `nil` if the action didn’t overwrite any item.
- `freeSpace`: An [`FSFreeSpace`](fsfreespace.md) instance populated with the volume’s updated free space. Passing a `nil` free space causes FSKit to calculate the free space when the operation is done, based on the volume’s [`volumeStatistics`](fsvolume/handler/volumestatistics.md) property. This behavior may lead to degraded performance.

## See Also

- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsrenameitemresult/init(newname:renameditemattributes:sourcedirectoryattributes:destinationdirectoryattributes:overitemattributes:freespace:))*