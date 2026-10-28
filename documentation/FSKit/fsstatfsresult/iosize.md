# ioSize

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A property for the optimal block size with which to perform I/O.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var ioSize: Int { get set }
```

```objc
@property NSInteger ioSize;
```

## Discussion

For best performance, specify an `ioSize` that’s an even multiple of [`blockSize`](./blocksize.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsstatfsresult/iosize)*