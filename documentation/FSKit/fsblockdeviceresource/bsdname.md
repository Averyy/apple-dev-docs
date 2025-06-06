# bsdName

**Framework**: FSKit  
**Kind**: property

The device name of the resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var bsdName: String { get }
```

## See Also

- [var isWritable: Bool](fsblockdeviceresource/iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockCount: UInt64](fsblockdeviceresource/blockcount.md)
  The block count on this resource.
- [var blockSize: UInt64](fsblockdeviceresource/blocksize.md)
  The logical block size, the size of data blocks used by the file system.
- [var physicalBlockSize: UInt64](fsblockdeviceresource/physicalblocksize.md)
  The sector size of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/bsdname)*