# length

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of bytes you choose to hold for this tensor data instance.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var length: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger length;
```

## Discussion

> ❗ **Important**:  This value must not exceed length of `bytes`.

## See Also

### Inspecting Tensor Data
- [var bytes: UnsafeMutableRawPointer](./bytes.md)
  A buffer that conains data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata/length)*