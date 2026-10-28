# SetPacketBufferPool

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

Assigns the specified buffer pool with this queue.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t SetPacketBufferPool(IOUserNetworkPacketBufferPool *pool);
```

## Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

## Discussion

Use this method to change the buffer pool that provides network packets to the queue. This method releases the previous pool, if any, and retains the new object in the `pool` parameter.

## Parameters

- `pool`: The new buffer pool to associate with the queue.

## See Also

### Configuring the Queue Attributes
- [SetPacketDirection](./setpacketdirection.md)
  Specifies whether packets flow into or out of the queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/setpacketbufferpool)*