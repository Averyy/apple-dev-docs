# isWritable

**Framework**: FSKit  
**Kind**: property

A Boolean property that indicates whether the resource can write data to the device.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var isWritable: Bool { get }
```

## See Also

- [var bsdName: String](fsblockdeviceresource/bsdname.md)
  The device name of the resource.
- [var blockCount: UInt64](fsblockdeviceresource/blockcount.md)
  The block count on this resource.
- [var blockSize: UInt64](fsblockdeviceresource/blocksize.md)
  The logical block size, the size of data blocks used by the file system.
- [var physicalBlockSize: UInt64](fsblockdeviceresource/physicalblocksize.md)
  The sector size of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/iswritable)*