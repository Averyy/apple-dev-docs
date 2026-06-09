# init(bytesAllocated:itemAttributes:freeSpace:)

**Framework**: FSKit  
**Kind**: init

Creates a result for a preallocate operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(bytesAllocated: Int, itemAttributes attributes: FSItem.Attributes, freeSpace: FSFreeSpace?)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `bytesAllocated`: The number of bytes actually allocated for the file during the preallocation operation.
- `attributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the file after the preallocation operation.
- `freeSpace`: An [`FSFreeSpace`](fsfreespace.md) instance populated with the volume’s updated free space. Passing a `nil` free space causes FSKit to calculate the free space when the operation is done, based on the volume’s [`volumeStatistics`](fsvolume/handler/volumestatistics.md) property. This behavior may lead to degraded performance.

## See Also

- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fspreallocateresult/init(bytesallocated:itemattributes:freespace:))*