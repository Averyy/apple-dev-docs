# length

**Framework**: ML Compute  
**Kind**: property

The number of bytes you choose to hold for this tensor data instance.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var length: Int { get }
```

#### Discussion

> ❗ **Important**:  This value must not exceed length of `bytes`.

 This value must not exceed length of `bytes`.

## See Also

- [var bytes: UnsafeMutableRawPointer](mlctensordata/bytes.md)
  A buffer that conains data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata/length)*