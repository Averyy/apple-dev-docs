# registerEthernetInterface

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit 24.0+

## Declaration

```swift
IOReturn registerEthernetInterface(ether_addr_t macAddress, IOUserNetworkPacketQueue * * queues, uint32_t numQueues, IOUserNetworkPacketBufferPool * txPool, IOUserNetworkPacketBufferPool * rxPool);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/registerethernetinterface-8pzu9)*