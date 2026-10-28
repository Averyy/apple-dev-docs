# init(freeSpace:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates a result for an extended-attribute-setting operation.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(freeSpace: FSFreeSpace?)
```

```objc
- (instancetype) initWithFreeSpace:(FSFreeSpace *) freeSpace;
```

## Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `freeSpace`: An [`FSFreeSpace`](../fsfreespace.md) instance populated with the volume’s updated free space. Passing a `nil` free space causes FSKit to calculate the free space when the operation is done, based on the volume’s [`volumeStatistics`](../fsvolume/handler/volumestatistics.md) property. This behavior may lead to degraded performance.

## See Also

### Creating a set-extended-attributes result
- [class FSFreeSpace](../fsfreespace.md)
  A free space object that pairs free space values with atomic sequence numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fssetxattrresult/init(freespace:))*