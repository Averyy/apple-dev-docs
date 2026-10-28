# physicalBlockSize

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

The sector size of the device.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var physicalBlockSize: UInt64 { get }
```

```objc
@property (readonly) uint64_t physicalBlockSize;
```

## Discussion

This is equivalent to the `DKIOCGETPHYSICALBLOCKSIZE` device parameter.

## See Also

### Accessing resource properties
- [var bsdName: String](./bsdname.md)
  The device name of the resource.
- [var isWritable: Bool](./iswritable.md)
  A Boolean property that indicates whether the resource can write data to the device.
- [var blockCount: UInt64](./blockcount.md)
  The block count on this resource.
- [var blockSize: UInt64](./blocksize.md)
  The logical block size, the size of data blocks used by the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsblockdeviceresource/physicalblocksize)*