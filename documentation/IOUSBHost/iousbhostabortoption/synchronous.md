# IOUSBHostAbortOption.synchronous

**Framework**: IOUSBHost  
**Kind**: case  
**Role**: Case

The option to abort input/output requests synchronously.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
case synchronous
```

```c
IOUSBHostAbortOptionSynchronous
```

#### Discussion

This is the default argument for functions that abort pending input/output requests. All input/output requests must abort before functions can return.

## See Also

### Options
- [IOUSBHostAbortOption.asynchronous](./asynchronous.md)
  The option to abort input/output requests asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostabortoption/synchronous)*