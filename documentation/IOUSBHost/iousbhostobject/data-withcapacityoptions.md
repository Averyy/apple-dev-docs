# data(withCapacity:options:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 26.4+

## Declaration

```swift
func data(withCapacity capacity: Int, options: IOUSBHostObjectDataOptions = []) throws -> NSMutableData
```

#### Return Value

NSMutableData of memory mapped to user space of an IOBufferMemoryDescriptor if successful, otherwise nil. An IOReturn error code will be reported on failure. The result is to be released by the caller

#### Discussion

Allocate a buffer to be used for I/O or an isochronous frame list.

This method will allocate and map an IOBufferMemoryDescriptor optimized for use by the underlying controller hardware. A buffer allocated by this method will not be bounced to perform DMA operations. Because the NSMutableData is backed by kernel memory, the length and capacity are not mutable. Any changes to the length or capacity will cause an exception to be thrown.

## Parameters

- `capacity`: Size of the buffer to allocate
- `options`: IOUSBHostObjectDataOptions. Default value is IOUSBHostObjectDataOptionsNone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/data(withcapacity:options:))*