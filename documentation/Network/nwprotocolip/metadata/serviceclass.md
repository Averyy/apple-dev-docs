# serviceClass

**Framework**: Network  
**Kind**: property  
**Role**: Instance Property

A specific service class to mark on an IP packet.

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
var serviceClass: NWParameters.ServiceClass { get set }
```

## See Also

### Related Documentation
- [var serviceClass: NWParameters.ServiceClass](../../nwparameters/serviceclass-swift.property.md)
  The traffic characteristics network connections send and receive.
### Sending IP Options
- [init()](./init%28%29.md)
  Initializes an IP packet configuration with default settings.
- [var ecn: NWProtocolIP.ECN](./ecn.md)
  A specific Explicit Congestion Notification flag value to set on an IP packet.
- [NWProtocolIP.ECN](../ecn.md)
  Flag values for Explicit Congestion Notifications in IP packets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nwprotocolip/metadata/serviceclass)*