# CopyMemoryDescriptor

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns a memory descriptor for the buffer pool’s contents.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t CopyMemoryDescriptor(IOMemoryDescriptor **memory);
```

## Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `memory`: On output, a pointer to a memory descriptor object. It is a programmer error to specify `NULL` or an invalid pointer for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool/copymemorydescriptor)*