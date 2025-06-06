# GetBufferCount

**Framework**: NetworkingDriverKit  
**Kind**: method

Returns the number of buffers associated with the network packet buffer pool.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t GetBufferCount(uint32_t * count);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `count`: On output, the number of buffers in the pool. It is a programmer error to specify   or an invalid pointer for this parameter.

## See Also

- [GetPacketCount](iousernetworkpacketbufferpool/getpacketcount.md)
  Returns the number of network packets that the pool is capable of storing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool/getbuffercount)*