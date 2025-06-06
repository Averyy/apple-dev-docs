# SetPacketDirection

**Framework**: NetworkingDriverKit  
**Kind**: method

Specifies whether packets flow into or out of the queue.

**Availability**:
- DriverKit ?+

## Declaration

```swift
kern_return_t SetPacketDirection(IOUserNetworkPacketDirection direction);
```

#### Return Value

`kIOReturnSuccess` on success, or another value if an error occurred.

#### Discussion

Typically, you do not call this method yourself. The concrete subclasses set the direction during initialization.

## Parameters

- `direction`: The direction for network packets to travel.

## See Also

- [SetPacketBufferPool](iousernetworkpacketqueue/setpacketbufferpool.md)
  Assigns the specified buffer pool with this queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkpacketqueue/setpacketdirection)*