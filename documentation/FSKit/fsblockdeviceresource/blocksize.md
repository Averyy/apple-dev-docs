# blockSize

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The logical block size, the size of data blocks used by the file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var blockSize: UInt64 { get }
```

```objc
@property (readonly) uint64_t blockSize;
```

## Discussion

This is equivalent to the `DKIOCGETBLOCKSIZE` device parameter.

## See Also

### Accessing resource properties
- [var bsdName: String](./bsdname.md)
  The device name of the resource.
- [var isWritable: Bool](./iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockCount: UInt64](./blockcount.md)
  The block count on this resource.
- [var physicalBlockSize: UInt64](./physicalblocksize.md)
  The sector size of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/blocksize)*