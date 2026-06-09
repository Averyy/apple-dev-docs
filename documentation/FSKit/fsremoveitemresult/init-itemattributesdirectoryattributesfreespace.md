# init(itemAttributes:directoryAttributes:freeSpace:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an item-removal operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(itemAttributes: FSItem.Attributes, directoryAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `itemAttributes`: The [`FSItem.Attributes`](fsitem/attributes.md) of the removed item.
- `directoryAttributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the parent directory.
- `freeSpace`: An [`FSFreeSpace`](fsfreespace.md) instance populated with the volume’s updated free space. Passing a `nil` free space causes FSKit to calculate the free space when the operation finishes, based on the volume’s [`volumeStatistics`](fsvolume/handler/volumestatistics.md) property. This behavior may lead to degraded performance.

## See Also

- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsremoveitemresult/init(itemattributes:directoryattributes:freespace:))*