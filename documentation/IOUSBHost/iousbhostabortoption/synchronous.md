# IOUSBHostAbortOption.synchronous

**Framework**: IOUSBHost  
**Kind**: case

The option to abort input/output requests synchronously.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
case synchronous
```

#### Discussion

This is the default argument for functions that abort pending input/output requests. All input/output requests must abort before functions can return.

## See Also

- [IOUSBHostAbortOption.asynchronous](iousbhostabortoption/asynchronous.md)
  The option to abort input/output requests asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostabortoption/synchronous)*