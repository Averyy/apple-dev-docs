# ioSize

**Framework**: FSKit  
**Kind**: property

A property for the optimal block size with which to perform I/O.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var ioSize: Int { get set }
```

#### Discussion

For best performance, specify an `ioSize` that’s an even multiple of [`blockSize`](fsstatfsresult/blocksize.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsstatfsresult/iosize)*