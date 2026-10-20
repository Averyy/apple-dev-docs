# size

**Framework**: DiskImageKit  
**Kind**: property  
**Role**: Instance Property

The logical size of the disk image in bytes.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var size: Int { get }
```

#### Discussion

This is equivalent to [`blockCount`](./blockcount.md) × [`blockSize`](./blocksize-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/size)*