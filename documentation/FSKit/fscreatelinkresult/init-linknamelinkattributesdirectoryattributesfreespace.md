# init(linkName:linkAttributes:directoryAttributes:freeSpace:)

**Framework**: FSKit  
**Kind**: init

Creates a result for a link-creation operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(linkName: FSFileName, linkAttributes: FSItem.Attributes, directoryAttributes: FSItem.Attributes, freeSpace: FSFreeSpace?)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `linkName`: The name of the newly-created hard link.
- `linkAttributes`: The [`FSItem.Attributes`](fsitem/attributes.md) of the linked item (the target of the hard link).
- `directoryAttributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the parent directory.
- `freeSpace`: An [`FSFreeSpace`](fsfreespace.md) instance populated with the volume’s updated free space. Passing a `nil` free space causes FSKit to calculate the free space when the operation is done, based on the volume’s [`volumeStatistics`](fsvolume/handler/volumestatistics.md) property. This behavior may lead to degraded performance.

## See Also

- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.
- [class FSFreeSpace](fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscreatelinkresult/init(linkname:linkattributes:directoryattributes:freespace:))*