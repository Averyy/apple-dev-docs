# registerEthernetInterface

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 24.0+

## Declaration

```cpp
virtual IOReturn registerEthernetInterface(ether_addr_t macAddress, IOUserNetworkPacketQueue **queues, uint32_t numQueues, IOUserNetworkPacketBufferPool *txPool, IOUserNetworkPacketBufferPool *rxPool);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/registerethernetinterface-8pzu9)*