# RegisterEthernetInterface

**Framework**: NetworkingDriverKit  
**Kind**: method

Registers your driver with the networking stack.

**Availability**:
- DriverKit ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
kern_return_t RegisterEthernetInterface(IOUserNetworkMACAddress macAddress, IOUserNetworkPacketBufferPool * pool, IOUserNetworkPacketQueue * * queues, uint32_t queueCount);
```

#### Discussion

Call this method toward the end of your [`Start`](https://developer.apple.com/documentation/DriverKit/IOService/Start) method when your driver is ready to begin processing incoming and outgoing network packets.

## Parameters

- `macAddress`: The MAC address of the hardware your driver supports.
- `pool`: The buffer pool you use to store incoming and outgoing packets.
- `queues`: An array containing the four queues you use to process incoming and outgoing network packets. This array must contain one queue each of types  ,  ,  , and  . The order of the queues in the array doesn’t matter.
- `queueCount`: The number of queues in the   parameter. The   parameter must contain 4 items.

## See Also

- [init](iousernetworkethernet/init.md)
  Handles the basic initialization of the service.
- [free](iousernetworkethernet/free.md)
  Performs any final cleanup for the service.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/registerethernetinterface-4jqw8)*