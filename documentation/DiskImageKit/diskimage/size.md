# size

**Framework**: DiskImageKit  
**Kind**: property

The logical size of the disk image in bytes.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var size: Int { get }
```

#### Discussion

This is equivalent to [`blockCount`](diskimage/blockcount.md) × [`blockSize`](diskimage/blocksize-swift.property.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/diskimagekit/diskimage/size)*