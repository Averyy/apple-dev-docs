# blockCount

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The block count on this resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var blockCount: UInt64 { get }
```

```objc
@property (readonly) uint64_t blockCount;
```

## See Also

### Accessing resource properties
- [var bsdName: String](./bsdname.md)
  The device name of the resource.
- [var isWritable: Bool](./iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockSize: UInt64](./blocksize.md)
  The logical block size, the size of data blocks used by the file system.
- [var physicalBlockSize: UInt64](./physicalblocksize.md)
  The sector size of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/blockcount)*