# bytes

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A buffer that conains data.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var bytes: UnsafeMutableRawPointer { get }
```

```objc
@property (nonatomic, readonly) void * bytes;
```

## See Also

### Inspecting Tensor Data
- [var length: Int](./length.md)
  The number of bytes you choose to hold for this tensor data instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordata/bytes)*