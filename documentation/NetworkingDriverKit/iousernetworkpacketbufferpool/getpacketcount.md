# GetPacketCount

**Framework**: NetworkingDriverKit  
**Kind**: method

Returns the number of network packets that the pool is capable of storing.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t GetPacketCount(uint32_t * count);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Parameters

- `count`: On output, the number of network packets supported by the pool. It is a programmer error to specify   or an invalid pointer for this parameter.

## See Also

- [GetBufferCount](iousernetworkpacketbufferpool/getbuffercount.md)
  Returns the number of buffers associated with the network packet buffer pool.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketbufferpool/getpacketcount)*