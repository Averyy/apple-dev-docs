# NWProtocolIP.ECN

**Framework**: Network  
**Kind**: enum

Flag values for Explicit Congestion Notifications in IP packets.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum ECN
```

## Topics

### ECN Flags
- [NWProtocolIP.ECN.nonECT](nwprotocolip/ecn/nonect.md)
  Non-ECN Capable Transport.
- [NWProtocolIP.ECN.ect0](nwprotocolip/ecn/ect0.md)
  ECN Capable Transport (flag 0).
- [NWProtocolIP.ECN.ect1](nwprotocolip/ecn/ect1.md)
  ECN Capable Transport (flag 1).
- [NWProtocolIP.ECN.ce](nwprotocolip/ecn/ce.md)
  Congestion Experienced.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init()](nwprotocolip/metadata/init.md)
  Initializes an IP packet configuration with default settings.
- [var ecn: NWProtocolIP.ECN](nwprotocolip/metadata/ecn.md)
  A specific Explicit Congestion Notification flag value to set on an IP packet.
- [var serviceClass: NWParameters.ServiceClass](nwprotocolip/metadata/serviceclass.md)
  A specific service class to mark on an IP packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolip/ecn)*