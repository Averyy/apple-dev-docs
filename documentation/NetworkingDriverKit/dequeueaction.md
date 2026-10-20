# DequeueAction

**Framework**: NetworkingDriverKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- DriverKit

## Declaration

```cpp
typedef unsigned int (*)(class OSObject *, class IOUserNetworkPacketQueue *, class IOUserNetworkPacket **, unsigned int, void *) DequeueAction;
```

## See Also

### Type aliases
- [EnqueueAction](./enqueueaction.md)
- [EventAction](./eventaction.md)
- [IONetworkPacketType](./ionetworkpackettype.md)
- [IOUserNetworkPacketLROFlags](./iousernetworkpacketlroflags.md)
- [IOUserNetworkPacketQueueId](./iousernetworkpacketqueueid.md)
- [IOUserNetworkPacketRxChecksumFlags](./iousernetworkpacketrxchecksumflags.md)
- [IOUserNetworkPacketTSOFlags](./iousernetworkpackettsoflags.md)
- [IOUserNetworkPacketTxChecksumFlags](./iousernetworkpackettxchecksumflags.md)
- [IOUserNetworkServiceClass](./iousernetworkserviceclass.md)
- [LinkQuality](./linkquality.md)
- [LinkStatus](./linkstatus.md)
- [MediaWord](./mediaword.md)
- [PollAction](./pollaction.md)
- [QueryFreeSpaceAction](./queryfreespaceaction.md)
- [ifdrv_t](./ifdrv_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/dequeueaction)*