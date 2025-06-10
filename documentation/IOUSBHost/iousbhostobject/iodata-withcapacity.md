# ioData(withCapacity:)

**Framework**: IOUSBHost  
**Kind**: method

Allocates a buffer for input/output requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func ioData(withCapacity capacity: Int) throws -> NSMutableData
```

#### Return Value

A pointer to an allocated buffer.

#### Discussion

This method allocates and maps a kernel buffer that the underlying controller hardware has optimized. Using this method, the buffer doesn’t bounce to perform DMA operations.

> ❗ **Important**:  Because the kernel backs the [`NSMutableData`](https://developer.apple.com/documentation/Foundation/NSMutableData) object, the length and capacity aren’t mutable. Any changes to the length or capacity throws an exception.

## Parameters

- `capacity`: The size, in bytes, of the buffer to allocate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/iodata(withcapacity:))*