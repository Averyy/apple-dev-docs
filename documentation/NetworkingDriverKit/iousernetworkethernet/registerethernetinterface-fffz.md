# RegisterEthernetInterface

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t RegisterEthernetInterface(ether_addr_t macAddress, IOUserNetworkPacketBufferPool * pool, IOUserNetworkPacketQueue * * queues, uint32_t queueCount);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/registerethernetinterface-fffz)*