# blockSize

**Framework**: FSKit  
**Kind**: property

The logical block size, the size of data blocks used by the file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var blockSize: UInt64 { get }
```

#### Discussion

This is equivalent to the `DKIOCGETBLOCKSIZE` device parameter.

## See Also

- [var bsdName: String](fsblockdeviceresource/bsdname.md)
  The device name of the resource.
- [var isWritable: Bool](fsblockdeviceresource/iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockCount: UInt64](fsblockdeviceresource/blockcount.md)
  The block count on this resource.
- [var physicalBlockSize: UInt64](fsblockdeviceresource/physicalblocksize.md)
  The sector size of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/blocksize)*