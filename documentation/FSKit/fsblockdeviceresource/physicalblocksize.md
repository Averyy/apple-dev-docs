# physicalBlockSize

**Framework**: FSKit  
**Kind**: property

The sector size of the device.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var physicalBlockSize: UInt64 { get }
```

#### Discussion

This is equivalent to the `DKIOCGETPHYSICALBLOCKSIZE` device parameter.

## See Also

- [var bsdName: String](fsblockdeviceresource/bsdname.md)
  The device name of the resource.
- [var isWritable: Bool](fsblockdeviceresource/iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockCount: UInt64](fsblockdeviceresource/blockcount.md)
  The block count on this resource.
- [var blockSize: UInt64](fsblockdeviceresource/blocksize.md)
  The logical block size, the size of data blocks used by the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/physicalblocksize)*