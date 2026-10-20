# blockSize

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

A property for the volume’s block size, in bytes.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var blockSize: Int { get set }
```

```objc
@property NSInteger blockSize;
```

#### Discussion

This value defaults to `4096`. Zero isn’t a valid block size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsstatfsresult/blocksize)*